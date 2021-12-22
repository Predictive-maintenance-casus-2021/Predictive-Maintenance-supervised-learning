from sklearn import preprocessing


def preprocess(data=None, add_time=True, labels=None):
    preprocessed_data = data.copy()

    if add_time:
        preprocessed_data = add_time_column(preprocessed_data)

    if labels is not None:
        preprocessed_data, label_encoders = add_label_encoding(preprocessed_data, labels)

        return preprocessed_data, label_encoders

    return preprocessed_data


def add_time_column(data=None):
    data["Time"] = data.apply(
        lambda row: row.name * 60, axis=1
    )

    col = data.pop("Time")
    data.insert(0, col.name, col)

    return data


def add_label_encoding(data=None, labels=None):
    label_encoding = {}
    if labels is not None:
        for label in labels:
            encoding = preprocessing.LabelEncoder()

            data[label] = encoding.fit_transform(data[label])

            label_encoding[label] = encoding

    return data, label_encoding


if __name__ == "__main__":
    print("This file cannot be directly run.")
