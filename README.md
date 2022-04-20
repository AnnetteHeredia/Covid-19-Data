# Covid-19 Data Flask App

![gif](https://media0.giphy.com/media/TjGV8ni2jC5pj6iY6T/giphy.gif?cid=ecf05e47y9n1wxob6r5xqw6jwu2oos5x0f569mhs87qbj2ne&rid=giphy.gif&ct=g)

## Table of contents

* [Coivd-19 Data](#covid-19-data)
* [Data Sources](#data-sources)
* [Technologies](#technologies)
* [Extract](#extract)
* [Transform](#transform)
* [Load](#load)
* [Visualizations](#visualizations)
* [Run Flask App](#run-flask)
* [Contacts](#contacts)

## Covid-19 Data

Objective: The objective was to present a more easily searchable Covid-19 data recorded throughout the heights of the pandemic by continent or by country and the date range.

## Data Sources

- [World Data](https://covid19.who.int/data)
- [United States](https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36)

## Technologies
* Python
* Flask
* Javascript
* HTML/CSS
* Plotly
* Jupyter Notebook
* SQLiteStudio

# Extract

* Find data sources via world data, united states (csvs)
* Jupyter Notebook to setup a logic, view, clean, and organize data with Pandas/Python

# Transform

* Transfer from CSV to SQLite
* We combined both US and World 

# Load

* Build Line Charts
* Build Leaflet maps, using javascript to use JSON API call
* Build Flask app and connectivity
 
# Deploy
 
* Using VSCode, we made an app to call our data queries from the SQLite database but call it using JSON call
* Data called, able to create visualizations for our build webpage viw CSS, Bootstrap, HTML, Javascript, Python

# Visualizations
 
<h2>Main Page

![before?](static/Images/mainpage.PNG)

Data Pulled in Main Page

![after?](static/Images/covid19html.png)

## Run Flask

To Deploy the Flask App, please follow the steps :
* step 1: Git clone the repository into your local

* step 2: Confirm that jupyter notebook is up and running with the env where you have the python libraries mentioned in the notebook installed

* step 3: Confirm that you have sqlitestudio app up and running in your machine

* step 4: Connect the database using the database called 'COVID_Data.db'

* step 5: Execute command python app.py and launch the server using URL: http://127.0.0.1:5000/

## Contacts

[Annette Heredia](https://github.com/AnnetteHeredia)

[Emanuel Villa](https://github.com/mannievilla)

[Johnathan Fludd](https://github.com/JohnathanFludd)

[Jordan Alonzo](https://github.com/jalonzoajordan)

[Miguel Martinez](https://github.com/mmtz97)

[Steven De Noia](https://github.com/Stencoss)
