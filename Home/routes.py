#!/usr/bin/env python3

# Importing the necessary modules
import os
import datetime
import sqlite3
from flask import request, jsonify
from flask import Blueprint, session, render_template
from Home.randomData import generate_random_data

# Creating the blueprint object
home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

# Creating a route for the home user
@home.route('/', methods=['GET', 'POST'])
def Home():
    # Display this for a get request
    if request.method == "GET":
        return render_template("Home.html")

    # Post request
    # elif request.method == "POST":
    #     return jsonify({"message": "POst request"})


# Simulate data
@home.route("/simulateData", methods=["POST"])
def SimulateData():
    # Create a database connection
    conn = sqlite3.connect('llmBenchmark.db')
    cursor = conn.cursor()

    # Getting the request data
    requestData = request.get_json()

    # Get the data
    llmModel = requestData["llmModel"]
    metrics = requestData["metrics"]
    dataPoints = int(requestData["dataPoints"])

    # Generating the data
    data = generate_random_data(
        llm_name=llmModel,
        metric_name=metrics,
        data_points=dataPoints
    )

    # Save data to database
    for item in data:
        cursor.execute('INSERT INTO llm_benchmark_results (llm_name, metric_name, result) VALUES (?, ?, ?)', (llmModel, metrics, item))

    # Saving the data
    conn.commit()

    # Returning the data
    return jsonify({
        "message": "Data created",
        "status": "success",
        "data": data,
    })
