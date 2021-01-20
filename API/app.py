from flask import Flask, request, redirect, url_for, flash, jsonify,render_template, url_for
import numpy as np
import json
import joblib


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
   
    Model = joblib.load(open('Model.sav', 'rb'))
    features = [str(x) for x in request.form.values()]
    final_features = [np.array(features)]
    output = Model.predict(final_features)

   
    return render_template('index.html', predictionValue='{}'.format(output[0]))


if __name__ == '__main__':
    app.run(port=5000,debug=True, host='localhost')