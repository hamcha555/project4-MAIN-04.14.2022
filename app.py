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

@app.route('/assessment.html')
def resources():
    return render_template("assessment.html")

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,2)
    loaded_model = pickle.load(open("model.pkl","rb")) # load the model
    result = loaded_model.predict(to_predict) # predict the values using loded model
    return result[0]

@app.route('/predict.html', methods = ['POST'])
def predict():
    int_features = [x for x in request.form.values()]

    l = len(int_features)
    print(l)

    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction = int(prediction.label[0])
    return render_template('/predict.html', pred = 'Expected Diagnosis: {}'.format(prediction))
    # return render_template('predict.html',prediction)

if __name__ == "__main__":
    app.run()