import os
import numpy as np
import tensorflow as tf
from joblib import dump, load
from .preprocess import DataTransformers


class ClassificationModel:
    def __init__(self, model, transformers):
        self.model = model
        self.transformers = transformers

    def predict(self, x):
        return self.inverse_y(self.model.predict(x))

    def save(self, name, path="./"):
        if not path.endswith("/"):
            path += "/"
        model_path = os.path.join(path, name.lower().replace(" ", "_"))

        self.model.save(model_path)
        dump(self.transformers.encoder, model_path + "/encoder.bin", compress=True)
        dump(self.transformers.x_scaler, model_path + "/x_scaler.bin", compress=True)
        dump(self.transformers.y_scaler, model_path + "/y_scaler.bin", compress=True)

    def inverse_x(self, x):
        return self.transformers.x_scaler.inverse_transform(x)

    def inverse_y(self, y):
        if y.ndim == 1:
            y = y.reshape(-1, 1)

        encoder_labels = self.transformers.encoder.transform(self.transformers.encoder.classes_)
        labels_id = np.round(self.transformers.y_scaler.inverse_transform(y)).astype(int).ravel()
        for i in range(0, len(labels_id)):
            if not labels_id[i] in encoder_labels:
                nearest_label = min(encoder_labels, key=lambda x: abs(x - labels_id[i]))
                print(f"[!] WARNING: Model made prediction {labels_id[i]}, which is not in the labels {encoder_labels}. This has been resolved by giving it the nearest value, which is {nearest_label}.")

                labels_id[i] = nearest_label

        inverse_encoder = self.transformers.encoder.inverse_transform(labels_id)

        return inverse_encoder


def load_model(path):
    model = tf.keras.models.load_model(path)

    encoder = load(path + "/encoder.bin")
    x_scaler = load(path + "/x_scaler.bin")
    y_scaler = load(path + "/y_scaler.bin")

    return ClassificationModel(
        model,
        DataTransformers(
            encoder,
            x_scaler,
            y_scaler
        )
    )
