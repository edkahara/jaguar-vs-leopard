# Image Classification: Jaguar vs Leopard

This image classifier will attempt to accurately distinguish between jaguars and leopards.

The model is [export.pkl](https://github.com/edkahara/jaguar-vs-leopard/tree/master/models/export.pkl).

The notebook [jaguar-vs-leopard.ipynb](https://github.com/edkahara/jaguar-vs-leopard/blob/master/notebooks/jaguar-vs-leopard.ipynb) shows how I trained the model, using [fastai](https://github.com/fastai/fastai)

Upload an image of either a jaguar or a leopard and click `Analyze` to see the model's prediction.

## How To Run The Application Locally

### Clone this repository

  `git clone https://github.com/edkahara/jaguar-vs-leopard.git`

### Change directories into your repository

  `cd jaguar-vs-leopard`

### Create a virtual environment

  `python3 -m venv env` or `py -3 -m venv env` for Windows.

### Set the environment variables

  `source env/bin/activate`

  `export FLASK_APP=app.py`

  or

  `env\Scripts\activate`

  `set FLASK_APP=app.py`

  for Windows.

### Install the packages needed

  `pip install -r local-requirements.txt`

### Run the application

  `flask run`

  Navigate to <http://localhost:5000> in your web browser to view the application.
