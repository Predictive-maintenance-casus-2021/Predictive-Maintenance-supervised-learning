import os
from maintenance_predictions import dataset, preprocess, evaluate, visualisation
from maintenance_predictions import model as mdl

if __name__ == "__main__":
    print("[!] Loading saved models...")
    models = {}
    for model in [[file.name.lower().replace(" ", "_"), file.path] for file in os.scandir("../models/") if file.is_dir()]:
        print(f"   [!] Loading {model[0]} model...")

        models[model[0]] = mdl.load_model(model[1])

    print("\n[!] Loading dataset...")
    dataset = dataset.load_dataset()

    print("\n[!] Preprocessing dataset...")
    preprocessed_data = preprocess.preprocess_data(
        dataset,
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
        test_size=0.2,
        history_window=15,
        future_window=30,
        shift=1,
        random_state=0
    )

    print("\n[!] Evaluating saved models...")
    for name, model in models.items():
        print("\n", name, "\n", "=" * 50, sep="")

        precision, recall, accuracy, f1_score = evaluate.evaluate_model(
            model,
            preprocessed_data[name].model_data.x_validation,
            preprocessed_data[name].model_data.y_validation
        )

        print(
            f"Precision: {precision}\n",
            f"Recall: {recall}\n",
            f"Accuracy: {accuracy}\n",
            f"F1-score: {f1_score}\n",
            sep=""
        )

        visualisation.confusion_matrix(
            model,
            preprocessed_data[name].model_data.x_validation,
            preprocessed_data[name].model_data.y_validation,
            name + " Confusion Matrix"
        ).show()
