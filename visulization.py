from flask import Flask, render_template, make_response,request,url_for,redirect
from datetime import datetime
import time
from ConsumerKafka import stockPrediction
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# url data to get data on index page
@app.route('/data', methods=['GET', 'POST'])
def data():
    prediction_result, close_value, data_time = stockPrediction()

    date_time = int(datetime.strptime(data_time, '%Y-%m-%d %H:%M:%S').strftime('%s')) * 1000

    data = [date_time, prediction_result, close_value]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    time.sleep(2)
    return response
if __name__=='__main__':
    app.run(debug=True, threaded=True)
