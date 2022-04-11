from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('log_regr_pipeline')
cols = ['']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/mentalhealth.html')
def mentalhealth():
    return render_template("mentalhealth.html")

@app.route('/resources.html')
def resources():
    return render_template("resources.html")

@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction = int(prediction.label[0])
    return render_template('home.html', pred = 'Expected Diagnosis: {}'.format(prediction))

if __name__ == "__main__":
    app.run()