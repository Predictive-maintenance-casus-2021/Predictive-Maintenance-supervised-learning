import numpy as np
from sklearn import metrics


def evaluate_model(model, x, y):
    y = model.inverse_y(y)
    y_predictions = model.predict(x)

    precision = metrics.precision_score(y, y_predictions, average=None, zero_division=0)
    recall = metrics.recall_score(y, y_predictions, average=None)
    accuracy = metrics.accuracy_score(y, y_predictions)
    f1_score = metrics.f1_score(y, y_predictions, average=None)

    return precision, recall, accuracy, f1_score
