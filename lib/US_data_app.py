#import python libraries
from flask import request
import sqlalchemy
from sqlalchemy import create_engine
import datetime
import json

#set up engine
engine = create_engine("sqlite:///./Data/COVID_Data.db")

def query_usa():
    #get primary data from webpage
    selected_state = request.form['selected_state']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    #get the parameters to run queries
    date_start_dt = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
    date_end_dt = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
    state_select = selected_state

    #create placeholders for data
    state_cases = []
    state_new = []
    state_tot_deaths = []
    state_new_death = []

    #due to SQL storing dates as string literals, create a list of dates to search from the range
    date_list = []
    date_delta = date_end_dt - date_start_dt

    for i in range(date_delta.days + 1):
        day = date_start_dt + datetime.timedelta(days=i)
        date_list.append(day.strftime("%m/%d/%Y"))
    date_list = tuple(date_list)
    print(date_list)

    #run queries for data
    #total cases by day
    state_cases_query = engine.execute(f"SELECT tot_cases FROM usa_data WHERE state = '{state_select}' AND submission_date IN {date_list} ORDER BY submission_date ASC").fetchall()
    for state in state_cases_query:
        state_cases.append(state[0])
    #new cases by day
    state_newcases_query = engine.execute(f"SELECT new_case FROM usa_data WHERE state = '{state_select}' AND submission_date IN {date_list} ORDER BY submission_date ASC").fetchall()
    for state in state_newcases_query:
        state_new.append(state[0])
    #total deaths by day
    state_totdeaths_query = engine.execute(f"SELECT tot_death FROM usa_data WHERE state = '{state_select}' AND submission_date IN {date_list} ORDER BY submission_date ASC").fetchall()
    for state in state_totdeaths_query:
        state_tot_deaths.append(state[0])
    #new deaths by day
    state_newdeaths_query = engine.execute(f"SELECT new_death FROM usa_data WHERE state = '{state_select}' AND submission_date IN {date_list} ORDER BY submission_date ASC").fetchall()
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
            'country' : 'USA',
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
    return json_string

def query_usa_range():
    #get primary data from webpage
    end_date = request.form['end_date']

    #get the parameters to run queries
    date_end_dt = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
    date_format = date_end_dt.strftime('%m/%d/%Y')

    #create placeholders for data
    state_cases = []
    state_tot_deaths = []

    #run queries for data
    #list of states with data on ending date
    state_list_query = engine.execute(f"SELECT state FROM usa_data WHERE submission_date = '{date_format}' ORDER BY submission_date ASC").fetchall()
    #total cases by day
    state_cases_query = engine.execute(f"SELECT tot_cases FROM usa_data WHERE submission_date = '{date_format}' ORDER BY submission_date ASC").fetchall()
    for state in state_cases_query:
        state_cases.append(state[0])
    #total deaths by day
    state_totdeaths_query = engine.execute(f"SELECT tot_death FROM usa_data WHERE submission_date = '{date_format}' ORDER BY submission_date ASC").fetchall()
    for state in state_totdeaths_query:
        state_tot_deaths.append(state[0])

    #take lists and create dictionary for JSON output
    i = 0
    output = []
    #match the day data into a dictionary
    while i < len(state_cases):
        #build the dictionary
        data_dict = {
            'country' : 'USA',
            'state' : state_list_query[i][0],
            'date': date_format,
            'total_cases': state_cases[i],
            'total_deaths': state_tot_deaths[i]
        }
        #append to file
        print(data_dict)
        output.append(data_dict)
        i=i+1

    #jsonify and return
    json_string = json.dumps(output)
    print(json_string)
    return json_string