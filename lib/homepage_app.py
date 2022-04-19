#import python libraries
import sqlalchemy
from sqlalchemy import create_engine

#set up engine
engine = create_engine("sqlite:///./Data/COVID_Data.db")

#Method to gather list of states for US state dropdown on form
def get_USlocations():
    state_query = engine.execute('SELECT DISTINCT(state) FROM usa_data ORDER BY state ASC').fetchall()
    states = []
    for loc in state_query:
        states.append(loc[0])
    return states

#Method to gather list of continents for World dropdown on form
def get_worldContinents():
    continent_query = engine.execute('SELECT DISTINCT(continent) FROM world_data ORDER BY continent ASC').fetchall()
    continents = []
    for loc in continent_query:
        continents.append(loc[0])
    return continents

#Method to gather list of countries for World dropdown on form
def get_worldCountries():
    country_query = engine.execute('SELECT DISTINCT(location) FROM world_data ORDER BY location ASC').fetchall()
    country = []
    for loc in country_query:
        country.append(loc[0])
    return country