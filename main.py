#first thing you need for flask

from flask import Flask, jsonify, render_template, redirect
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json


#dEcribe where the application is being run from
app = Flask(__name__)


#trick for annotation a finctiionality to  in Python add  @  it tells it the route "/"
@app.route("/")

#simple function that returns this statement
def index():
    return "Welcome to Get Leaf!"

#telling the route and that it need to run this function
@app.route("/about")

#simple function that returns this statement
def about():
    return "Welcome to the About page!"

#last piece we need, useful of launching from gitbash it will be name but if running from cloud service it may be "main"
if __name__ == "__main__":
    app.run(debug=True)




# the basic boiler plate shell for app.py
# from flask import Flask, jsonify

# app = Flask(__name__)



# if __name__ == "__main__":
#     app.run(debug=True)