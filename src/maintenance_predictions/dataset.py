import os
import pandas as pd


def load_dataset(path=None):
    if path is None:
        path = os.path.split(os.path.realpath(__file__))[0] + os.sep + "data"

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

    dataset["Time"] = dataset.apply(
        lambda row: row.name * 60, axis=1
    )
    col = dataset.pop("Time")
    dataset.insert(0, col.name, col)

    return dataset
