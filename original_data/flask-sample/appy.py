from flask import Flask, render_template
import requests
from pprint import pprint

app = app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/test')
def test():
    return 'Test'


if __name__ =='__main__':
    app.run()
