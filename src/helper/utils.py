import os
import numpy as np
import pandas as pd


def load_dataset(path="./data/"):
    files = [file for file in os.listdir(path) if file.endswith(".txt") and file != "documentation.txt" and
             file != "description.txt" and file != "profile.txt"]

    dataset = pd.DataFrame()

    for file in files:
        dataset[file.strip(".txt")] = pd.read_csv(
            os.path.join(path, file),
            sep="\t",
            header=None
        ).mean(axis=1).to_numpy()

    profiles = ["Cooler condition", "Valve condition", "Internal pump leakage", "Hydraulic accumulator", "Stable flag"]
    for i, profile in enumerate(profiles):
        dataset[profile] = pd.read_csv(
            os.path.join(path, "profile.txt"),
            sep="\t",
            header=None,
        )[i].to_numpy()

    return dataset


def inverse_transform(data=None, scaler=None, encoder=None):
    transformed_data = data.copy()

    if scaler is not None:
        if transformed_data.ndim == 1:
            transformed_data = transformed_data.reshape(-1, 1)

        transformed_data = scaler.inverse_transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.inverse_transform(np.round(transformed_data).astype(int).ravel())

    return transformed_data


def get_file_name(name):
    return name.lower().replace(" ", "_")


if __name__ == "__main__":
    print("This file cannot be directly run.")