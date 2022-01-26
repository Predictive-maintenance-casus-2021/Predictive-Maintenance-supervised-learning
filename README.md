# Hydraulic Systems Predictive Maintenance

A predictive maintenance proof-of-concept which uses machine learning (Long-Short Term Memory) to predict maintenance for hydraulic systems. 
This repo includes:

* A Jupyter Notebook which explains generating a model and predictions for one target-variable,
* A web interface using VueJS and Flask (Python backend),
* a few python scripts which the web interface uses, but can be used as standalone scripts to generate models and predictions.

## 1. Editing/contributing

### 1.1. Jupyter Notebook

Either install [Jupyter notebook with mamba, conda, or pip](https://jupyter.org/install). 

### 1.2. Web server

#### 1.2.1. Anaconda
We advise installing the packages for this repository using Anaconda, there is an option to install this using pip but this can cause issues.
- Step 1. Clone this repository onto your machine. 
- Step 2. Download and install [Anaconda](https://anaconda.com).
- Step 3. Open the Anaconda Powershell Prompt.
- Step 4. In your terminal navigate to the folder you cloned the repository into `cd "filelocation"`.
- Step 5. Execute the command `conda env create -f requirements_conda.yml` and install the required packages..
- Step 6. Activate your installed environment using `conda activate BD04`.
- Step 6. In your terminal navigate to the `cd src/web` folder.
- Step 7. Execute the `python main.py` command while in your Anaconda environment and the src/web folder.

#### 1.2.2. PIP
Installing the application this way can cause issues.

#### 1.2.3. NPM
These steps are **optional** and only need to be done if you are planning on **changing** the frontend.
- Step 1. Clone this repository onto your machine if you have not done this yet. 
- Step 2. Download and install [NPM](https://nodejs.org/en/download/), we recommend installing the LTS version.
- Step 3. Go to `/src/web/vue/` in your command prompt of choice.
- Step 4. Execute the command `npm install`, to install all the packages used for the frontend.
- Step 5. Now you can run the command `npm run serve` to run a development build of the app. When you have finished developing the frontend you can run `npm run build` to have it replace the items on the Flask server.

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

