from flask import Flask, jsonify, render_template, redirect
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json



app =Flask(__name__)

@app.route("/")
def home():
    print("Am I working?")
    # Home Page
    # return ("index.html")
    return render_template("index.html")



# Route that will return Web API JSON data from SQLite
# Route to world_data
# TODO: Find the queries that I need
@app.route("/world_leaf_api")
def world_leaf_api():
    # session = Session(engine)


    conn = sqlite3.connect(f'Data/COVID_Data.db') 
    cursor = conn.cursor()
    cursor.execute("SELECT location, total_cases, total_deaths FROM world_data WHERE date = \"2022-03-01\" ")
    results = cursor.fetchall()

    # print(results[0][0])

    conn.close()

    return (jsonify(results))

# ROute to world_leaf page
@app.route("/world_leaf")
def world_leaf():
    return render_template("world.html")

@app.route('/allgeojson')
def allgeojson():
    f = open('all.geojson')
    load = json.load(f)
    return load

if __name__ == "__main__":
    app.run(debug=True)