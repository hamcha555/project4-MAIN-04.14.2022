from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# model = load_model('log_regr_pipeline')
cols = ['']

model = "log_regr_pipeline.pkl"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/detecting.html')
def mentalhealth():    
    return render_template("detecting.html")
# def predict():
#   input_values = [float(x) for x in request.form.values()]
#   inp_features = [input_values]
#   prediction = model.predict(inp_features)
#   if prediction==1:
#     return render_template('/detecting.html', prediction_text='Death event took Place. Person is no more')
#   else:
#     return render_template('/detecting.html', prediction_text='Death event not took Place. Person is alive')

@app.route('/resources.html')
def resources():
    return render_template("resources.html")

# @app.route('/predict.html')
# def predict():
#     return render_template("/predict.html")

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,2)
    loaded_model = pickle.load(open(model,"rb")) # load the model
    result = loaded_model.predict(to_predict) # predict the values using loded model
    return result[0]

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        int_features = [x for x in request.form.values()]

        # l = len(int_features)
        # print(l)

        final = np.array(int_features)
        data_unseen = pd.DataFrame([final], columns = cols)
        prediction = int_features[0]
        # prediction = predict_model(model, data=data_unseen, round = 0)
        # prediction = int(prediction.label[0])
        # return render_template('/predict.html', pred = 'Expected Diagnosis: {}'.format(prediction))
        return render_template('/detecting.html',prediction_test = prediction)
    else:
        return render_template('/')
# @app.route('/result', methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = ValuePredictor(to_predict_list)       
#         if int(result)== 1:
#             prediction ='Please get help - you may suffer from depression'
#         else:
#             prediction ='You are not likely to suffer from depression'           
#         return render_template("/detecting.html", prediction = prediction)

# @app.route('/detecting.html', methods=['GET', "POST"])


if __name__ == "__main__":
    app.run()