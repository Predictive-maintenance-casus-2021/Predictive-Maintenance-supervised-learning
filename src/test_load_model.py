from helper.utils import *
from helper.model.evaluate import *
from helper.model.creation.preprocess import *
from helper.model.creation.train import *


if __name__ == "__main__":
    models = {}
    print(load_model("cooler_condition", "../models/"))
