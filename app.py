from flask import Flask, request, render_template, jsonify
from fastai import *
from fastai.vision import *
from io import BytesIO

app = Flask(__name__)

path = Path('./models')

learn = load_learner(path)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file'].read()
    img = open_image(BytesIO(file))
    prediction = learn.predict(img)[0]
    response = {'result': str(prediction)}
    return jsonify(response)
