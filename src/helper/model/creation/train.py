import os
import numpy as np
from joblib import dump
import tensorflow as tf
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from helper.utils import *


class TrainResult:
    def __init__(self, model, x_scaler, y_scaler, x_train, y_train, x_validation, y_validation):
        self.model = model
        self.x_scaler = x_scaler
        self.y_scaler = y_scaler
        self.encoder = None
        self.x_train = x_train
        self.y_train = y_train
        self.x_validation = x_validation
        self.y_validation = y_validation

    def set_encoder(self, encoder):
        self.encoder = encoder


def train(x_data, y_data, epochs=10, test_size=0.2, history_window=5, future=0, shift=1, encoder=None):
    x_data, x_scaler = scale_data(x_data)
    y_data, y_scaler = scale_data(y_data)

    x_data_grouped, y_data_grouped = group_data(x_data, y_data, history_window, future, shift)

    x_train, x_validation, y_train, y_validation = train_test_split(
        x_data_grouped,
        y_data_grouped,
        test_size=test_size,
        random_state=1
    )

    model = make_model(x_train.shape[1], x_train.shape[2])
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=10,
        mode='min'
    )

    model.fit(
        x_train,
        y_train,
        epochs=epochs,
        validation_data=(x_validation, y_validation),
        callbacks=[early_stopping]
    )

    result = TrainResult(
        model,
        x_scaler,
        y_scaler,
        x_train,
        y_train,
        x_validation,
        y_validation
    )

    if encoder is not None:
        result.set_encoder(encoder)

    return result


def train_multiple_models(data=None, models=None, epochs=10, test_size=0.2, history_window=5, future=0, shift=1, encoders=None):
    train_results = {}
    for y, x in models.items():
        encoder = None
        if encoders is not None:
            for name, instance in encoders.items():
                if name == y:
                    encoder = instance
                    break

        train_results[y] = train(data[x], data[[y]], epochs, test_size, history_window, future, shift, encoder)

    return train_results


def scale_data(data=None):
    scaler = preprocessing.MinMaxScaler()

    return scaler.fit_transform(data), scaler


def group_data(x_data=None, y_data=None, history_window=5, future=0, shift=1):
    if not isinstance(x_data, np.ndarray) or not isinstance(y_data, np.ndarray):
        raise Exception("Data has to be a NumPy array.")

    num_batches = np.int((np.floor((len(x_data) - history_window) / shift)) + 1 - future)
    num_features = x_data.shape[1]

    x_output = np.repeat(np.nan, repeats=num_batches * history_window * num_features).reshape(num_batches,
                                                                                              history_window,
                                                                                              num_features)
    if y_data is None:
        for batch in range(num_batches):
            x_output[batch, :, :] = x_data[(0 + shift * batch):(0 + shift * batch + history_window), :]

        return x_output

    y_output = np.repeat(np.nan, repeats=num_batches)
    for batch in range(num_batches):
        x_output[batch, :, :] = x_data[(0 + shift * batch):(0 + shift * batch + history_window), :]
        y_output[batch] = y_data[(shift * batch + (history_window - 1)) + future]

    return x_output, y_output


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


def save_model(train_result=None, name=None, path="./models/"):
    model_path = os.path.join(path, get_file_name(name))

    train_result.model.save(model_path)

    dump(train_result.encoder, f"{model_path}/label_encoder.bin", compress=True)
    dump(train_result.x_scaler, f"{model_path}/x_scaler.bin", compress=True)
    dump(train_result.y_scaler, f"{model_path}/y_scaler.bin", compress=True)


if __name__ == "__main__":
    print("This file cannot be directly run.")
