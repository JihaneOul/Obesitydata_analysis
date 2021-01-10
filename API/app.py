from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
import joblib


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return 'Hello this is the API'


@app.route('/predict', methods=['POST'])
def pred():
    data = request.get_json()
    prediction = Model.predict(data)

    #Making sure the target values are also under json format. 

    NObesity = {
        0:"Insufficient Weight", 
        1:"Normal Weight", 
        2:"Overweight Level I", 
        3:"Overweight Level II",
        4:"Obesity Type I",
        5:"Obesity Type II",
        6:"Obesity Type III"}
    return jsonify(prediction)

if __name__ == '__main__':
    Model = joblib.load(open('Model.sav', 'rb'))
    print('Model loaded')
    app.run(port=5000,debug=True, host='localhost')