import os
import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn import metrics
from joblib import load
from helper.utils import *
from helper.utils import inverse_transform
from helper.model.creation.train import TrainResult


def load_model(name=None, path="./models"):
    model_path = os.path.join(path, get_file_name(name))

    model = tf.keras.models.load_model(model_path)
    encoder = load(f"{model_path}/label_encoder.bin")
    x_scaler = load(f"{model_path}/x_scaler.bin")
    y_scaler = load(f"{model_path}/y_scaler.bin")

    return model, encoder, x_scaler, y_scaler


def get_evaluation_metrics(train_result=None):
    check_train_result(train_result)

    y_validation = inverse_transform(train_result.y_validation, train_result.y_scaler, train_result.encoder)
    y_predictions = inverse_transform(train_result.model.predict(train_result.x_validation), train_result.y_scaler, train_result.encoder)

    precision = metrics.precision_score(y_validation, y_predictions, average=None),
    recall = metrics.recall_score(y_validation, y_predictions, average=None)
    accuracy = metrics.accuracy_score(y_validation, y_predictions)
    f1_score = metrics.f1_score(y_validation, y_predictions, average=None)

    return precision[0], recall, accuracy, f1_score


def get_confusion_matrix(train_result=None, name=None):
    check_train_result(train_result)

    figure = plt.figure()

    y_validation = inverse_transform(train_result.y_validation, train_result.y_scaler, train_result.encoder)
    y_predictions = inverse_transform(train_result.model.predict(train_result.x_validation), train_result.y_scaler, train_result.encoder)

    categories = np.unique([y_validation, y_predictions])

    cf_matrix = metrics.confusion_matrix(y_validation, y_predictions)

    sns.heatmap(
        cf_matrix / np.sum(cf_matrix),
        annot=True,
        xticklabels=categories,
        yticklabels=categories,
        cmap="Greens",
        fmt=".2%",
        cbar=False
    )

    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Prediction")
    plt.ylabel("Actual")

    return figure


def check_train_result(train_result):
    if train_result is None or not isinstance(train_result, TrainResult):
        raise ValueError("Train results needs to be of type TrainResult.")


if __name__ == "__main__":
    print("This file cannot be directly run.")
