from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper

#init app and class
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

# #endpoint
# # Favicon
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                           'favicon.ico',mimetype='image/vnd.microsoft.icon')

#Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# Route to render index.html template
@app.route("/team")
def about():
    # Return template and data
    return render_template("team.html")

# Route to render index.html template
@app.route("/visualizations")
def visualizations():
    # Return template and data
    return render_template("visualizations.html")

@app.route("/predictions")
def predictions():
    # Return template and data
    return render_template("predictions.html")

@app.route("/analysis")
def analysis():
    # Return template and data
    return render_template("analysis.html")

@app.route("/resources")
def resources():
    # Return template and data
    return render_template("resources.html")

@app.route("/data")
def data():
    # Return template and data
    return render_template("data.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    content = request.json["data"]

    # parse
    acc = float(content["acc"])
    mph = float(content["mph"])
    range = float(content["range"])
    seats = int(content["seats"])
    fast_charge = int(content["fast_charge"])
    body_style = (content["body_style"])
    drive = content["drive"]

   

    prediction = modelHelper.makePredictions(acc, mph, range, seats, body_style, drive, fast_charge)
    print(prediction)
    return(jsonify({"ok": True, "prediction": str(prediction)}))
    

####################################
# ADD MORE ENDPOINTS

###########################################

#############################################################

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     return r

#main
if __name__ == "__main__":
    app.run(debug=True)
