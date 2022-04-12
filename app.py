from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# model = "log_regr_pipeline.pkl"
# print(model)

model = pickle.load(open("log_regr_pipeline.pkl","rb"))
cols = ['']
prediction = "Test"


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/detecting.html')
def mentalhealth():    
    return render_template("detecting.html")

@app.route('/resources.html')
def resources():
    return render_template("resources.html")

# prediction function
# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,2)
#     loaded_model = pickle.load(open("model.pkl","rb")) # load the model
#     result = loaded_model.predict(to_predict) # predict the values using loded model
#     return result[0]

# @app.route('/predict', methods = ["POST"])
@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [x for x in request.form.values()]

    # l = len(int_features)
    # print(l)

    # final = np.array(int_features)
    # prediction = model.predict(final)
    prediction = int_features[0]
    # prediction = "Test"


    # data_unseen = pd.DataFrame([final], columns = cols)
    # prediction = predict_model(model, data=data_unseen, round = 0)
    # prediction = int(prediction.label[0])
    # return render_template('/predict.html', pred = 'Expected Diagnosis: {}'.format(prediction))
    # return render_template('/detecting.html',prediction)
    return render_template('/detecting.html', prediction_text = "The number of hours worked is {}".format(prediction))
    # return render_template('/detecting.html')



if __name__ == "__main__":
    app.run()