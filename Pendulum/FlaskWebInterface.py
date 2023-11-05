from flask import Flask, render_template, request, redirect, flash, jsonify, make_response
from flask_classful import FlaskView, route
from werkzeug.utils import secure_filename
from json import JSONEncoder
from DataContainer import DataContainer
import time

app = Flask(__name__)


class TestView(FlaskView):
    app.secret_key = "einsZweiDreiVier"

    #loading the html template
    @route("/")
    def index(self):
        #return "HELLO"
        return render_template("index.html")

    #route for the fetch api, running on the website
    @route("/api/data", methods = ['GET', 'POST'])
    def prepareJson(self):
        DC = DataContainer.getInstance()
        curStatus = {
            'lastTime': DC.lastTime,
            'currentA': DC.MeasurementA,
            'currentB': DC.MeasurementB
        }
        message = {
            'status': curStatus,
            'list': DC.measurementList
        }
        encoder = JSONEncoder()
        returnvalue = encoder.encode(message)
        return returnvalue

    #testfuntction for debugging
    @route('/test')
    def test(self):
        return "Hello this is the measurement page."


TestView.register(app, route_base='/')

#start webinterface open or closed to network
def startWebInterface(openToNetwork=False):
    if openToNetwork == True:
        app.run(host='0.0.0.0', port=9000, debug=False)
    else:
        app.run()
