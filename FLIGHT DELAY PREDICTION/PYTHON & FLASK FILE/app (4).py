import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('flightdelay.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def pred():
    flnum = request.form['flnum']
    print(flnum)
    month1 = request.form['month']
    print(month1)
    dayofmonth = request.form['daymonth']
    print(dayofmonth)
    dayofweek = request.form['dayofweek']
    print(dayofweek)
    origin = request.form['origin']
    print(origin)
    dest1 = request.form['dest']
    print(dest1)
    arrtime = request.form['arrivaltime']
    print(arrtime)
    depdelay = request.form['depdelay']
    print(depdelay)
    inp_features = [[int(int(flnum)), int(month1), int(dayofmonth), int(dayofweek),
                     int(origin), int(dest1),
                     int(arrtime),int(depdelay)]]
    print(inp_features)
    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'Chance of delay'
    else:
        prediction_text = 'No chance of delay'
    print(prediction_text)
    return render_template('prediction.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
