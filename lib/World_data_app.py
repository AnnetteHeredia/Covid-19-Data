#import python libraries
from flask import request
import sqlalchemy
from sqlalchemy import create_engine
import datetime
import json

# Create engine using the `demographics.sqlite` database file
engine = create_engine("sqlite:///./Data/COVID_Data.db")
conn = engine.connect()

def query_continent():
    #get primary data from webpage
    continent_select = request.form['selected_continent']
    start_date = request.form['start_date_continent']
    end_date = request.form['end_date_continent']

    #get the parameters to run queries
    date_start_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    date_end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    #due to SQL storing dates as string literals, create a list of dates to search from the range
    date_list = []
    date_delta = date_end_dt - date_start_dt

    for i in range(date_delta.days + 1):
        day = date_start_dt + datetime.timedelta(days=i)
        date_list.append(day.strftime('%Y-%m-%d'))
    date_list = tuple(date_list)

    if len(date_list) < 2:
        date_list = (f"('{date_start_dt.strftime('%Y-%m-%d')}')")

    #create placeholders for continent data
    continent_cases = []
    continent_new = []
    continent_tot_deaths = []
    continent_new_death = []
    continent_dates = []
    
    #dates of all rows retrieved
    continent_dates_query = engine.execute(f"SELECT date FROM world_data WHERE continent = '{continent_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for continent in continent_dates_query:
        continent_dates.append(continent[0])

    #total cases by day
    continent_cases_query = engine.execute(f"SELECT total_cases FROM world_data WHERE continent = '{continent_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for continent in continent_cases_query:
        continent_cases.append(continent[0])
    
    #new continent cases by day
    continent_newcases_query = engine.execute(f"SELECT new_cases FROM world_data WHERE continent = '{continent_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for continent in continent_newcases_query:
        continent_new.append(continent[0])

    #total continent deaths by day
    continent_totdeaths_query = engine.execute(f"SELECT total_deaths FROM world_data WHERE continent = '{continent_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for continent in continent_totdeaths_query:
        continent_tot_deaths.append(continent[0])

    #new continent deaths by day
    continent_newdeaths_query = engine.execute(f"SELECT new_deaths FROM world_data WHERE continent = '{continent_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for continent in continent_newdeaths_query:
        continent_new_death.append(continent[0])

    #take lists and create continent dictionary for JSON output
    i = 0
    curr_date = date_start_dt - datetime.timedelta(days = 1)
    continent_output = []
    #match the day data into a dictionary
    while i < len(date_list):
        #get the date
        curr_date = curr_date + datetime.timedelta(days = 1)
        str_date  = str(curr_date)
        #get the list of indexes for the current date
        curr_date_indexes = [x for x in range(len(continent_dates)) if continent_dates[x] == str_date]
        #use these indexes to summarize all countries in the selected continent for that date
        #total cases
        total_cases_list =  [continent_cases[j] for j in curr_date_indexes if continent_cases[j] != '']
        total_cases = sum(total_cases_list)
        #new cases
        total_newcases_list =  [continent_new[j] for j in curr_date_indexes if continent_new[j] != '']
        new_cases = sum(total_newcases_list)
        #total deaths
        total_deaths_list =  [continent_tot_deaths[j] for j in curr_date_indexes if continent_tot_deaths[j] != '']
        total_deaths = sum(total_deaths_list)
        #new deaths
        total_newdeaths_list =  [continent_new_death[j] for j in curr_date_indexes if continent_new_death[j] != '']
        new_deaths = sum(total_newdeaths_list)
        #build the dictionary
        continent_data_dict = {
            'country' : continent_select,
            'state' : continent_select,
            'date': str_date,
            'total_cases': total_cases,
            'new_cases': new_cases,
            'total_deaths': total_deaths,
            'new_deaths': new_deaths
        }
        #append to file
        continent_output.append(continent_data_dict)
        i=i+1
    
    #jsonify and send out continent data
    json_string = json.dumps(continent_output)
    return json_string

def query_Country():
    #get primary data from webpage
    country_select = request.form['selected_country']
    start_date = request.form['start_date_country']
    end_date = request.form['end_date_country']

    #get the parameters to run queries
    date_start_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    date_end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    #due to SQL storing dates as string literals, create a list of dates to search from the range
    date_list = []
    date_delta = date_end_dt - date_start_dt

    for i in range(date_delta.days + 1):
        day = date_start_dt + datetime.timedelta(days=i)
        date_list.append(day.strftime('%Y-%m-%d'))
    date_list = tuple(date_list)

    if len(date_list) < 2:
        date_list = f"('{date_start_dt.strftime('%Y-%m-%d')}')"

    #create placeholders for country data
    country_cases = []
    country_new = []
    country_tot_deaths = []
    country_new_death = []

    #run queries for country data
    #continent
    continent_query = engine.execute(f"SELECT DISTINCT(continent) FROM world_data WHERE location = '{country_select}'").fetchone()

    #total cases by day
    country_cases_query = engine.execute(f"SELECT total_cases FROM world_data WHERE location = '{country_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for country in country_cases_query:
        country_cases.append(country[0])
    
    #new country cases by day
    country_newcases_query = engine.execute(f"SELECT new_cases FROM world_data WHERE location = '{country_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for country in country_newcases_query:
        country_new.append(country[0])

    #total country deaths by day
    country_totdeaths_query = engine.execute(f"SELECT total_deaths FROM world_data WHERE location = '{country_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for country in country_totdeaths_query:
        country_tot_deaths.append(country[0])

    #new country deaths by day
    country_newdeaths_query = engine.execute(f"SELECT new_deaths FROM world_data WHERE location = '{country_select}' AND date IN {date_list} ORDER BY date ASC").fetchall()
    for country in country_newdeaths_query:
        country_new_death.append(country[0])

    #take lists and create country dictionary for JSON output
    i = 0
    curr_date = date_start_dt - datetime.timedelta(days = 1)
    country_output = []
    #match the day data into a dictionary
    while i < len(country_cases):
        #get the date
        curr_date = curr_date + datetime.timedelta(days = 1)
        str_date  = str(curr_date)
        print(curr_date)
        #build the dictionary
        country_data_dict = {
            'country' : continent_query[0],
            'state' : country_select,
            'date': str_date,
            'total_cases': country_cases[i],
            'new_cases': country_new[i],
            'total_deaths': country_tot_deaths[i],
            'new_deaths': country_new_death[i]
        }
        #append to file
        country_output.append(country_data_dict)
        i=i+1
    
    #jsonify and send out country data
    json_string = json.dumps(country_output)
    return json_string

def query_world_range():
    #get primary data from webpage
    try:
        end_date = request.form['end_date_continent']
        #get the parameters to run queries
        date_end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        date_format = date_end_dt.strftime('%Y-%m-%d')
    except:
        end_date = request.form['end_date_country']
        #get the parameters to run queries
        date_end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        date_format = date_end_dt.strftime('%Y-%m-%d')

    #create placeholders for data
    state_cases = []
    state_tot_deaths = []

    #run queries for data
    #list of states with data on ending date
    location_list_query = engine.execute(f"SELECT location FROM world_data WHERE date = '{date_format}' ORDER BY location ASC").fetchall()
    continent_list_query = engine.execute(f"SELECT continent FROM world_data WHERE date = '{date_format}' ORDER BY location ASC").fetchall()
    #total cases by day
    world_cases_query = engine.execute(f"SELECT total_cases FROM world_data WHERE date = '{date_format}' ORDER BY location ASC").fetchall()
    for state in world_cases_query:
        state_cases.append(state[0])
    #total deaths by day
    world_totdeaths_query = engine.execute(f"SELECT total_deaths FROM world_data WHERE date = '{date_format}' ORDER BY location ASC").fetchall()
    for state in world_totdeaths_query:
        state_tot_deaths.append(state[0])

    #take lists and create dictionary for JSON output
    i = 0
    output = []
    #match the day data into a dictionary
    while i < len(state_cases):
        #build the dictionary
        data_dict = {
            'country' : continent_list_query[i][0],
            'state' : location_list_query[i][0],
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