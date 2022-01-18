import os
import numpy as np
import tensorflow as tf
from joblib import dump


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

        inverse_scaler = self.transformers.y_scaler.inverse_transform(y)
        inverse_encoder = self.transformers.encoder.inverse_transform(np.round(inverse_scaler).astype(int).ravel())

        return inverse_encoder


def train_model(data, epochs=100, early_stopping_patience=10):
    model = make_model(data.model_data.x_train.shape[1], data.model_data.x_train.shape[2])

    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        mode="min",
        patience=early_stopping_patience
    )

    model.fit(
        data.model_data.x_train,
        data.model_data.y_train,
        validation_data=(data.model_data.x_validation, data.model_data.y_validation),
        epochs=epochs,
        callbacks=[early_stopping]
    )

    return ClassificationModel(model, data.data_transformers)


def train_multiple_model(data, epochs=100, early_stopping_patience=10):
    models = {}
    for name, train_data in data.items():
        models[name] = train_model(train_data, epochs, early_stopping_patience)

    return models


def make_model(n_history_window, n_features):
    tf.keras.backend.set_floatx('float64')

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, input_shape=(n_history_window, n_features), return_sequences=True,
                             activation="tanh"),
        tf.keras.layers.LSTM(64, activation="tanh", return_sequences=True),
        tf.keras.layers.LSTM(32, activation="tanh"),
        tf.keras.layers.Dense(96, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        loss=tf.losses.MeanSquaredError(),
        optimizer=tf.optimizers.Adam(),
        metrics=[tf.metrics.MeanAbsoluteError()]
    )

    return model
