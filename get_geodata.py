import json
import requests


def get_world_data():
    f = open('all.geojson')
    load = json.load(f)
    return load


print(get_world_data())