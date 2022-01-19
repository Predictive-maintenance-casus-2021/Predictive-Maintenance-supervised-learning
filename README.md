# Hydraulic Systems Predictive Maintenance

A predictive maintenance proof-of-concept which uses machine learning (Long-Short Term Memory) to predict maintenance for hydraulic systems. 
This repo includes:

* A Jupyter Notebook which explains generating a model and predictions for one target-variable,
* A web interface using VueJS and Flask (python backend),
* a few python scripts which the web interface uses, but can be used as standalone scripts to generate models and predictions.

## 1. Editing/contributing

In order to edit the source code, you'll need to install the required languages, packages, etc.

Step 1. Get (at least) [Python version 3.7.8](https://www.python.org/downloads/)

step 2. Clone this repo onto your machine. If you use PIP, we recommend creating a [python virtual environment](https://docs.python.org/3/tutorial/venv.html)

Step 3. [Install all neccesary packages from the requirements.txt file.](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from)

### 1.1. Jupyter Notebook

Either install [Jupyter notebook with mamba, conda, or pip](https://jupyter.org/install). 

### 1.2. Web server

Iets over vuejs, flask, etc installeren @cedric

### 1.3. Standalone python files

The files are split into 5;

* PredictiveMaintenancePipeline.py: The main python file which calls upon all other python files. This is the file that should be run.
* utils.py: Contains methods for loading and transforming data, enabling the data to be used in other files.
* preprocess.py: pre-processes the data; checks for errors, adds label encoding, etc.
* train.py: Trains the model(s)
* evaluate.py: contains methods for calculating and displaying model/prediciton metrics.



## 2. Running the application

### 2.1. Jupyter Notebook

Make sure you've installed [Jupyter notebook with mamba, conda, or pip](https://jupyter.org/install). 
If you want to launch the notebook, pen a terminal and navigate to the folder of this repo on your machine launch the notebook by running `jupyter notebook` in your terminal

### 2.2. Web server

@cedric iets zeggen over de webserver, of je dit met docker doet ofzo. minimale om te runnen

### 2.3. Standalone python files

If you want to run the standalone python files, run the python file in the `/src/` folder; PredictiveMaintenancePipeline.py. Running other python files in any other (sub) folder will not work. Make sure to have followed the installation instructions in chapter 1.

## Data

The data in this repo was provided by https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems#

