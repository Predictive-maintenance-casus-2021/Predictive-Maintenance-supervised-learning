import os
import webbrowser
from threading import Thread
import time
from flask import Flask
from src.maintenance_predictions import dataset, preprocess, evaluate, visualisation
from src.maintenance_predictions import model as mdl

app = Flask(__name__)

# Prediction variables
models = {}
x_data = {}
y_predictions = {}


@app.route("/api/predictions")
def get_predictions():
    return {
        "cooler_condition": y_predictions.get("cooler condition")[-1],
        "valve_condition": y_predictions.get("valve condition")[-1],
        "internal_pump_leakage": y_predictions.get("internal pump leakage")[-1],
        "hydraulic_accumulator": y_predictions.get("hydraulic accumulator")[-1]
    }


@app.route("/api/predictions/history")
def get_history_predictions():
    return {
        "cooler_condition": y_predictions.get("cooler condition"),
        "valve_condition": y_predictions.get("valve condition"),
        "internal_pump_leakage": y_predictions.get("internal pump leakage"),
        "hydraulic_accumulator": y_predictions.get("hydraulic accumulator")
    }


@app.route("/api/stats/{model}")
def get_stats(model):
    return {
        "precision": [],
        "recall": [],
        "accuracy": [],
        "f1_score": []
    }


@app.route("/api/stats/{model}/confusion")
def get_confusion_matrix(model):
    print("!")


# ToDo: need to edit later
@app.route("/api/make_model")
def make_model(lookback, future, patience, early_stopping, epochs, shift):
    print("[!] Making model")
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
    for model in [[file.name.replace("_", " "), file.path] for file in os.scandir("../../models") if file.is_dir()]:
        print(f"   [!] Loading {model[0]} model...")

        models[model[0]] = mdl.load_model(model[1])
        y_predictions[model[0]] = []


def load_data():
    print("[!] Loading and preprocessing dataset...")
    all_models_data = preprocess.preprocess_data(
        dataset.load_dataset(),
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
        # TODO: put this data in config file
        test_size=0.2,
        history_window=15,
        future_window=30,
        shift=1,
        random_state=0,
        shuffle=False
    )

    for name, data in all_models_data.items():
        Thread(target=load_new_data_every_loop, args=(name, data.model_data.x_validation,)).start()

    print("[!] Dataset has been loaded and preprocessed...")


def load_new_data_every_loop(name, data, i=1):
    global x_data, y_predictions

    # Get new data for time.
    x_data[name] = data[:i]

    # Make predictions on new data
    pred = int(models.get(name).predict(x_data.get(name))[0])
    y_predictions.get(name).append(pred)

    print(f"[!] {name}: iteration {i}, pred: {pred}, list: {y_predictions.get(name)}")

    time.sleep(10)
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
    # Laad de getrainde modellen in.
    load_models()

    # Laad de data in die gebruikt wordt voor de voorspellingen.
    Thread(target=load_data).start()

    # Automatically open the browser, if the reload has not yet run
    # TODO: turn on when build is done (keep of while developing)
    # if not os.environ.get("WERKZEUG_RUN_MAIN"):
    #     webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", use_reloader=False)
