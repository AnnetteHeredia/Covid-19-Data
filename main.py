#first thing you need for flask

from flask import Flask, jsonify, render_template, redirect, request
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json

import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect, func
import datetime



#dEcribe where the application is being run from
app = Flask(__name__)

database_path = "Data/COVID_Data.db"

engine = create_engine(f"sqlite:///{database_path}")


#trick for annotation a finctiionality to  in Python add  @  it tells it the route "/"
@app.route("/")

#simple function that returns this statement
def index():
    return render_template('./index.html')

#telling the route and that it need to run this function
@app.route("/about")

#simple function that returns this statement
def about():
    return "Welcome to the About page!"



@app.route('/getTotalDeathByAllState', methods=['GET'])
def getTotalDeathByAlltate():
    database_path = "Data/COVID_Data.db"

    engine = create_engine(f"sqlite:///{database_path}")

    cases_data = engine.execute("SELECT tot_cases, state FROM (SELECT tot_cases, state, ROW_NUMBER() OVER(PARTITION BY state ORDER BY submission_date DESC) as row_num FROM usa_data) table1 WHERE row_num = 1;")

    deaths_data = engine.execute("SELECT tot_death, state FROM (SELECT tot_death, state, ROW_NUMBER() OVER(PARTITION BY state ORDER BY submission_date DESC) as row_num FROM usa_data) table1 WHERE row_num = 1;")

    return jsonify(
        {
            'status' : 'success',
            'results' :{
                'cases' : [ case_data.values() for case_data in cases_data ],
                'deaths' : [ death_data.values() for death_data in deaths_data ]
            }
        })

@app.route('/getTotalDeathByOnetate', methods=['GET'])
def getTotalDeathByOneState():
    state = request.args.get('state') or ''

    case_data = engine.execute("SELECT tot_cases, state FROM usa_data WHERE state = \"" + state + "\" ORDER BY submission_date DESC LIMIT 1;")
    death_data = engine.execute("SELECT tot_death, state FROM usa_data WHERE state =\"" + state + "\" ORDER BY submission_date DESC LIMIT 1;")

    return jsonify(
        {
            'status' : 'success',
            'result' :{
                'cases' : [ cd.values() for cd in case_data ],
                'deaths' : [ dd.values() for dd in death_data ],
                'state': state
            }
        })

#last piece we need, useful of launching from gitbash it will be name but if running from cloud service it may be "main"
if __name__ == "__main__":
    app.run(debug=True)




# the basic boiler plate shell for app.py
# from flask import Flask, jsonify

# app = Flask(__name__)



# if __name__ == "__main__":
#     app.run(debug=True)



# Dependencies and Setup


# File to Load (Remember to Change These)

database_path = "Data/COVID_Data.db"


engine = create_engine(f"sqlite:///{database_path}")



cases_data = engine.execute("SELECT tot_cases, state FROM (SELECT tot_cases, state, ROW_NUMBER() OVER(PARTITION BY state ORDER BY submission_date DESC) as row_num FROM usa_data) table1 WHERE row_num = 1;")


deaths_data = engine.execute("SELECT tot_death, state FROM (SELECT tot_death, state, ROW_NUMBER() OVER(PARTITION BY state ORDER BY submission_date DESC) as row_num FROM usa_data) table1 WHERE row_num = 1;")


