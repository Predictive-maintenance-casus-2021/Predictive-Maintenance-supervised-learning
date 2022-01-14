import numpy as np
from sklearn import preprocessing, model_selection


class TrainData:
    def __init__(self, model_data, data_transformers):
        self.model_data = model_data
        self.data_transformers = data_transformers


class ModelData:
    def __init__(self, x_train, y_train, x_validation, y_validation):
        self.x_train = x_train
        self.y_train = y_train
        self.x_validation = x_validation
        self.y_validation = y_validation


class DataTransformers:
    def __init__(self, encoder, x_scaler, y_scaler):
        self.encoder = encoder
        self.x_scaler = x_scaler
        self.y_scaler = y_scaler


def preprocess_data(df, labels, test_size=0.2, history_window=10, future_window=30, shift=1, random_state=1):
    preprocessed_df = df.copy()

    data = {}
    for y, x in labels.items():
        y_data, encoder = add_label_encoding(preprocessed_df[y])

        x_data, x_scaler = add_data_scaling(preprocessed_df[x])
        y_data, y_scaler = add_data_scaling(y_data.reshape(-1, 1))

        x_data, y_data = add_data_groups(x_data, y_data, history_window, future_window, shift)

        x_train, x_validation, y_train, y_validation = model_selection.train_test_split(
            x_data,
            y_data,
            test_size=test_size,
            random_state=random_state
        )

        model_data = ModelData(x_train, y_train, x_validation, y_validation)
        data_transformers = DataTransformers(encoder, x_scaler, y_scaler)

        data[y] = TrainData(
            model_data,
            data_transformers
        )

    return data


def add_label_encoding(data):
    encoder = preprocessing.LabelEncoder()
    data = encoder.fit_transform(data)

    return data, encoder


def add_data_scaling(df):
    scaler = preprocessing.MinMaxScaler()

    return scaler.fit_transform(df), scaler


def add_data_groups(x_data, y_data, history_window=5, future_window=0, shift=1):
    if not isinstance(x_data, np.ndarray) or not isinstance(y_data, np.ndarray):
        raise Exception("Data has to be a NumPy array.")

    num_batches = np.int((np.floor((len(x_data) - history_window) / shift)) + 1 - future_window)
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
        y_output[batch] = y_data[(shift * batch + (history_window - 1)) + future_window]

    return x_output, y_output
