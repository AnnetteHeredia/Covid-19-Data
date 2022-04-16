#import python libraries
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import sqlalchemy
from sqlalchemy import create_engine
import datetime
import json

#Set up Flask
app = Flask(__name__)

#set up engine
engine = create_engine("sqlite:///./Data/COVID_Data.db")


#Create Flask Routes
@app.route("/")
def home(*args):
    if len(args) > 0:
        print(f"ARGS ------ {args[0]}")
        json_string = args[0]
    else:
        json_string = {}
    return render_template("US_Charts_Only.html", json_data = json_string)
    

@app.route("/query_USA", methods=['POST','GET'])
def query_usa():
    #get primary data from webpage
    selected_state = request.form['selected_state']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    #get the parameters to run queries
    date_start_dt = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
    state_select = selected_state

    #create placeholders for data
    state_cases = []
    state_new = []
    state_tot_deaths = []
    state_new_death = []

    #run queries for data
    #total cases by day
    state_cases_query = engine.execute(f"SELECT tot_cases FROM usa_data WHERE state = '{state_select}' AND submission_date BETWEEN '{start_date}' AND '{end_date}'").fetchall()
    for state in state_cases_query:
        state_cases.append(state[0])
    #new cases by day
    state_newcases_query = engine.execute(f"SELECT new_case FROM usa_data WHERE state = '{state_select}' AND submission_date BETWEEN '{start_date}' AND '{end_date}'").fetchall()
    for state in state_newcases_query:
        state_new.append(state[0])
    #total deaths by day
    state_totdeaths_query = engine.execute(f"SELECT tot_death FROM usa_data WHERE state = '{state_select}' AND submission_date BETWEEN '{start_date}' AND '{end_date}'").fetchall()
    for state in state_totdeaths_query:
        state_tot_deaths.append(state[0])
    #new deaths by day
    state_newdeaths_query = engine.execute(f"SELECT new_death FROM usa_data WHERE state = '{state_select}' AND submission_date BETWEEN '{start_date}' AND '{end_date}'").fetchall()
    for state in state_newdeaths_query:
        state_new_death.append(state[0])

    #take lists and create dictionary for JSON output
    i = 0
    curr_date = date_start_dt - datetime.timedelta(days = 1)
    output = []
    #match the day data into a dictionary
    while i < len(state_cases):
        #get the date
        curr_date = curr_date + datetime.timedelta(days = 1)
        str_date  = str(curr_date)
        #build the dictionary
        data_dict = {
            'state' : selected_state,
            'date': str_date,
            'total_cases': state_cases[i],
            'new_cases': state_new[i],
            'total_deaths': state_tot_deaths[i],
            'new_deaths': state_new_death[i]
        }
        #append to file
        print(data_dict)
        output.append(data_dict)
        i=i+1

    #jsonify and return
    json_string = json.dumps(output)
    print(json_string)
    return home(json_string)

if __name__ == "__main__":
    app.run(debug=True)