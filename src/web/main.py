import os
import sys
import webbrowser
from flask import Flask

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maintenance_predictions import dataset, preprocess

app = Flask(__name__)
x_data = {}


@app.route("/api/predictions")
def get_predictions():
    return {
        "cooler_condition": 0,
        "valve_condition": 0,
        "internal_pump_leakage": 0,
        "hydraulic_accumulator": 0
    }


@app.route("/api/predictions/history")
def get_history_predictions():
    return {
        "cooler_condition": [],
        "valve_condition": [],
        "internal_pump_leakage": [],
        "hydraulic_accumulator": []
    }


@app.route("/api/stats/{model}")
def get_stats(model):
    return {
        "precision": [],
        "recall": [],
        "accuracy": [],
        "f1_score": []
    }


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


def load_data():
    global x_data

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
        random_state=0
    )

    for name, data in all_models_data.items():
        print(name, data.model_data.x_validation, data.model_data.y_validation)

    print("[!] Dataset has been loaded and preprocessed...")


def load_new_data_every_loop(dataset):

    print("!")

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
    # Laad de data in die gebruikt wordt voor de voorspellingen.
    load_data()

    # Automatically open the browser, if the reload has not yet run
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", use_reloader=False)
