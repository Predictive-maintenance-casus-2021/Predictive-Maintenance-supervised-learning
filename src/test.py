from helper.utils import *
from helper.model.evaluate import *
from helper.model.creation.preprocess import *
from helper.model.creation.train import *


if __name__ == "__main__":
    print("[!] Loading dataset...")

    dataset = load_dataset("../data/")

    print("[!] Preprocessing dataset...")

    preprocessed_dataset, label_encoders = preprocess(
        dataset,
        labels=["Cooler condition", "Valve condition", "Internal pump leakage", "Hydraulic accumulator"]
    )

    print("[!] Training model with preprocessed dataset.")

    train_results = train_multiple_models(
        preprocessed_dataset,
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
        epochs=25,
        test_size=0.2,
        history_window=30,
        future=0,
        shift=1,
        encoders=label_encoders
    )

    print("[!] Evaluating trained models.")

    for name, train_result in train_results.items():
        # Save model to specified path.
        # save_model(train_result.model, name, "../models/")

        # Get scores

        print(f"\n{name}")
        print("=" * 50)

        precision, recall, accuracy, f1_score = get_evaluation_metrics(train_result)
        print(
            f"Precision: {precision}",
            f"Recall: {recall}",
            f"Accuracy: {accuracy}",
            f"F1-score: {f1_score}",
            sep="\n"
        )

        # Get Confusion matrix of categorical predictions.
        figure = get_confusion_matrix(train_result, name=name)
        plt.show()
