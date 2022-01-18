import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics


def confusion_matrix(model, x, y, name="Confusion Matrix"):
    y = model.inverse_y(y)
    y_predictions = model.predict(x)

    fig = plt.figure()
    labels = np.unique([y, y_predictions])
    labels.sort()

    cf_matrix = metrics.confusion_matrix(
        y_true=y,
        y_pred=y_predictions,
        labels=labels
    )

    sns.heatmap(
        cf_matrix / np.sum(cf_matrix),
        annot=True,
        cmap="Greens",
        fmt=".2%",
        cbar=False,
        xticklabels=labels,
        yticklabels=labels
    )

    plt.title(name)
    plt.xlabel("Prediction")
    plt.ylabel("Actual")

    return fig
