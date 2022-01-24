import io
import os
import webbrowser
from threading import Thread
import time
import numpy as np
from flask import Flask, abort, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from src.maintenance_predictions import dataset, preprocess, evaluate, visualisation, train
from src.maintenance_predictions import model as mdl

app = Flask(__name__)

# Prediction variables
models = {}
y_predictions = {}

# Model evaluation
x_val_data = {}
y_val_data = {}

# Config file to save data
config = {}


# ToDo: pip install yaml
def load_config():
    print("config will be loaded")


@app.route("/api/predictions")
def get_predictions():
    predictions = {}

    for model in y_predictions:
        model_predictions = y_predictions.get(model)
        if model_predictions:
            predictions[model] = model_predictions[-1]

    return predictions


@app.route("/api/predictions/history")
def get_history_predictions():
    predictions = {}

    for model in y_predictions:
        predictions[model] = y_predictions.get(model)

    return predictions


@app.route("/api/stats/<model>")
def get_stats(model):
    if not model in models or not model in x_val_data or not model in y_val_data:
        abort(400, "Model with name " + model + " not found.")

    precision, recall, accuracy, f1_score = evaluate.evaluate_model(
        models[model],
        x_val_data[model],
        y_val_data[model]
    )

    for i in range(0, len(precision)):
        precision[i] = np.round(precision[i] * 100, 2)
        recall[i] = np.round(recall[i] * 100, 2)
        f1_score[i] = np.round(f1_score[i] * 100, 2)

    accuracy = np.round(accuracy * 100, 2)

    return {
        "precision": precision.tolist(),
        "recall": recall.tolist(),
        "accuracy": accuracy.tolist(),
        "f1_score": f1_score.tolist()
    }


@app.route("/api/stats/<model>/confusion")
def get_confusion_matrix(model):
    if model not in models or model not in x_val_data or model not in y_val_data:
        abort(400, "Model with name " + model + " not found.")

    confusion_matrix = visualisation.confusion_matrix(
        models[model],
        x_val_data[model],
        y_val_data[model],
        model.replace("_", " ").title() + " Confusion Matrix"
    )

    output = io.BytesIO()
    FigureCanvasAgg(confusion_matrix).print_png(output)

    return Response(output.getvalue(), mimetype="image/png")


# ToDo: need to edit later
@app.route("/api/make_model")
def make_model(lookback, future, patience, early_stopping, epochs, shift):
    print("[!] Making model")

    new_model = train.train_multiple_model(
        # ToDo: fill this in.
    )
    return ''


# ToDo: add the specific value's
@app.route("/api/import")
def import_models():
    return {
        print("[!] Get model")
    }


def load_models():
    global models, y_predictions

    print("[!] Loading saved models...")
    for model in [[file.name.lower().replace(" ", "_"), file.path] for file in os.scandir("../../models") if
                  file.is_dir()]:
        print(f"   [!] Loading {model[0]} model...")

        models[model[0]] = mdl.load_model(model[1])
        y_predictions[model[0]] = []


def load_data():
    global x_val_data, y_val_data

    print("[!] Loading and preprocessing dataset...")

    data = dataset.load_dataset()
    labels = {
        # Used correlation of <= -0.5 or >= 0.5
        "Cooler condition": ["Time", "CE", "EPS1", "FS2", "PS5", "TS1", "VS1"],
        # Used correlation of <= -0.05 or >= 0.05
        "Valve condition": ["Time", "FS1", "PS3", "PS4", "SE", "VS1"],
        # Used correlation of <= -0.25 or >= 0.25
        "Internal pump leakage": ["Time", "FS1", "PS3", "SE", "VS1"],
        # Used correlation of <= -0.20 or >= 0.20
        "Hydraulic accumulator": ["Time", "CE", "CP", "PS5", "TS2"],
        # Might be added in the future.
        # "Stable flag": []
    }
    test_size = 0.2
    history_window = 15
    future_window = 30
    shift = 1
    random_state = 0

    models_data = preprocess.preprocess_data(
        data,
        labels,
        test_size,
        history_window,
        future_window,
        shift,
        random_state,
        shuffle=False
    )
    evaluation_data = preprocess.preprocess_data(
        data,
        labels,
        test_size,
        history_window,
        future_window,
        shift,
        random_state,
        shuffle=True
    )

    for name, data in models_data.items():
        x_val_data[name] = evaluation_data[name].model_data.x_validation
        y_val_data[name] = evaluation_data[name].model_data.y_validation

        # make a thread for loading te data every x seconds.
        Thread(target=load_new_data_every_loop, args=(name, data.model_data.x_validation,)).start()

    print("[!] Dataset has been loaded and preprocessed...")


def load_new_data_every_loop(name, data, i=1):
    global y_predictions

    # Get data for predictions.
    x_data = data[:i]

    # Make predictions on data.
    prediction = models.get(name).predict(x_data)
    y_predictions.get(name).append(int(prediction[-1]))

    if i < len(data):
        time.sleep(5)
        load_new_data_every_loop(name, data, i + 1)


# Allows communication between the front and backend server
# TODO: get rid of when build fully
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == "__main__":
    # Load the trained models.
    load_models()

    # Load the data that's used for predictions.
    Thread(target=load_data).start()

    # Automatically open the browser, if the reload has not yet run
    # TODO: turn on when build is done (keep of while developing)
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/api/predictions')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", use_reloader=False)
