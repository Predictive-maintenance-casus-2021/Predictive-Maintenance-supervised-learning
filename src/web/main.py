import os
import sys
import io
import yaml
import webbrowser
from threading import Thread
import time
import numpy as np
from flask import Flask, Response, request, abort, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Imported this way to make sure the module can be found.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maintenance_predictions import dataset, preprocess, evaluate, visualisation, train
from maintenance_predictions import model as mdl

app = Flask(__name__)

# Prediction variables
models = {}
y_predictions = {}

# Model evaluation
x_val_data = {}
y_val_data = {}

# Config file to save data
config = {}


#
# Routes
#


@app.route("/")
def index():
    return render_template("index.html")


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


@app.route("/api/model/create", methods=["POST"])
def make_model():
    global models, y_predictions, x_val_data, y_val_data, config
    print("[!] Starting to train new models...")

    data = request.get_json()

    # Test size is default 20%.
    test_size = 0.2
    history_window = data.get("history_window", 15)
    future_window = data.get("future_window", 30)
    shift = data.get("shift", 1)
    random_state = data.get("random_state", 0)

    early_stopping_patience = data.get("patience", 5)
    epochs = data.get("epochs", 25)

    print("[!] Loading dataset...")
    df = dataset.load_dataset()

    print("\n[!] Preprocessing dataset...")
    preprocessed_data = preprocess.preprocess_data(
        df,
        {
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
        },
        test_size=test_size,
        history_window=history_window,
        future_window=future_window,
        shift=shift,
        random_state=random_state
    )

    print("\n[!] Training models...")
    trained_models = train.train_multiple_model(
        preprocessed_data,
        epochs=epochs,
        early_stopping_patience=early_stopping_patience
    )

    print("\n[!] Evaluating models...")
    for name, model in trained_models.items():
        confusion_matrix = visualisation.confusion_matrix(
            model,
            preprocessed_data[name].model_data.x_validation,
            preprocessed_data[name].model_data.y_validation,
            name + " Confusion Matrix"
        )

        save_model = True
        while save_model is None:
            save_input = input("\n[!] Do you want to save this model? (Y/N) ").casefold()
            if save_input == "y".casefold():
                save_model = True
            elif save_input == "n".casefold():
                save_model = False

        if save_model:
            print(f"   [!] Saving {name} model...")

            model.save(name, "../../models")
            confusion_matrix.savefig("../../models/" + name.replace(" ", "_").lower() + "/confusion_matrix")

    with open("config.yml", 'w') as file:
        config["saved_model_location"] = "../../models"
        config["model"]["future_window"] = future_window
        config["model"]["history_window"] = history_window
        config["model"]["random_state"] = random_state
        config["model"]["shift"] = shift
        yaml.dump(config, file)

    # Prediction variables
    models = {}
    y_predictions = {}

    # Model evaluation
    x_val_data = {}
    y_val_data = {}

    # Restarting the backend when there is a nieuw model made.
    print("restart backend")
    load_models()
    # Load the data that's used for predictions.
    Thread(target=load_data).start()

    return "Done"


#
# Loading essential items for running the application.
#


def load_config():
    global config

    print("[!] Loading yml config...")
    with open("config.yml", "r") as stream:
        config = yaml.safe_load(stream)


def load_models():
    global models, y_predictions

    print("[!] Loading saved models...")
    for model in [[file.name.lower().replace(" ", "_"), file.path] for file in
                  os.scandir(config.get("saved_model_location", "../../best_models")) if
                  file.is_dir()]:
        print(f"   [!] Loading {model[0]} model...")

        models[model[0]] = mdl.load_model(model[1])
        y_predictions[model[0]] = []


def load_data():
    global x_val_data, y_val_data, config

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
    saved_model_location = config.get("saved_model_location", "../../best_models")
    if saved_model_location == "../../best_models":
        test_size = config.get("best_model.test_size", 0.2)
        history_window = config.get("best_model.history_window", 15)
        future_window = config.get("best_model.future_window", 30)
        shift = config.get("best_model.shift", 1)
        random_state = config.get("best_model.random_state", 0)
    else:
        test_size = config.get("model.test_size", 0.2)
        history_window = config.get("model.history_window", 15)
        future_window = config.get("model.future_window", 30)
        shift = config.get("model.shift", 1)
        random_state = config.get("model.random_state", 0)

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
    model = models.get(name)
    if model:
        prediction = models.get(name).predict(x_data)
        y_predictions.get(name).append(int(prediction[-1]))

        if i < len(data):
            time.sleep(config.get("app.interval", 5))
            load_new_data_every_loop(name, data, i + 1)


if __name__ == "__main__":
    # Load the settings for models
    load_config()

    # Load the trained models.
    load_models()

    # Load the data that's used for predictions.
    Thread(target=load_data).start()

    # Automatically open the browser, if the reload has not yet run
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(host="", port=5000, use_reloader=False)
