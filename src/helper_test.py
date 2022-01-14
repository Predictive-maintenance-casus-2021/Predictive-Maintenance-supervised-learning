from maintenance_predictions import dataset, preprocess, train, evaluate

if __name__ == "__main__":
    print("[!] Loading dataset...")
    dataset = dataset.load_dataset()

    print("[!] Preprocessing dataset...")
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

    print("[!] Training models...")
    models = train.train_multiple_model(
        preprocessed_data,
        epochs=5,
        early_stopping_patience=10
    )

    print("[!] Evaluating models...")
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

    dataset.head()
