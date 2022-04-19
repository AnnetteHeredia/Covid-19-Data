#import python libraries
from flask import Flask, render_template, jsonify
from lib import homepage_app, World_data_app, US_data_app
import sqlalchemy
from sqlalchemy import create_engine
import json
import sqlite3

#Set up Flask
app = Flask(__name__)

#homepage
@app.route("/")
def home(*args):
    print("Page accessed: Home")
    states = homepage_app.get_USlocations()
    continents = homepage_app.get_worldContinents()
    countries = homepage_app.get_worldCountries()
    return render_template("index.html", states = states, continents = continents, countries = countries)
    
#Continent Selection Route
@app.route("/query_Continent", methods=['POST', 'GET'])
def query_Continent():
    print("Page accessed: Continent data")
    json_data = World_data_app.query_continent()
    map_data = World_data_app.query_world_range()
    return render_template("Queried_Data.html", json_data = json_data, map_data = map_data)

#Continent Selection Route
@app.route("/query_Country", methods=['POST', 'GET'])
def query_Country():
    print("Page accessed: Continent data")
    json_data = World_data_app.query_Country()
    map_data = World_data_app.query_world_range()
    return render_template("Queried_Data.html", json_data = json_data, map_data = map_data)

#USA Selection Route
@app.route("/query_USA", methods=['POST','GET'])
def query_USA():
    print("Page accessed: US Data")
    json_data = US_data_app.query_usa()
    map_data = US_data_app.query_usa_range()
    return render_template("Queried_Data.html", json_data = json_data, map_data = map_data)

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

@app.route('/allgeojson')
def allgeojson():
    f = open('static/js/all.geojson')
    load = json.load(f)
    return load

#run the app
if __name__ == "__main__":
    app.run(debug=True)