# Libraries and dependencies
import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import asc, desc

from flask import Flask, jsonify

#######################
# Database connection
#######################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Connect
session = Session(engine)

#############
# API Code
#############

app = Flask(__name__)

@app.route("/")
def index():
    print("Server received request for 'Home' page...")
    return (f"<h1>Welcome to the Hawaii Climate API, available routes:</h1></br>"
    f"/api/v1.0/stations <a href = /api/v1.0/stations>JSON station list</a></br>"
    f"/api/v1.0/tobs <a href = /api/v1.0/tobs>JSON temperatures from the most active station for the past 12 months</a></br>"
    f"/api/v1.0/&ltstart&gt &ltstart&gt is a date which you want to retrieve stats from, for example <a href = /api/v1.0/2017-05-23>2017-05-23</a></br>"
    f"/api/v1.0/&ltstart&gt/&ltend>&gt start and end are the date range you want to retrieve stats from, for example <a href = /api/v1.0/2016-08-23/2017-08-23>From 2016-08-23 to 2017-08-23</a></br>")

@app.route("/api/v1.0/stations")
def stations():
    # Creating the query
    stations = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation)
    session.close()

    # Building the list
    sta_list = []
    for _ in stations:
        sta_list.append(_)

    # List of stations
    return jsonify(sta_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Determining number of days (leap-year logic)
    
    # Querying the DB
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    # Unpacking the result
    last_date = [last_date[0] for _ in last_date]

    # Converting date to string
    last_date = str(last_date[0])

    # Converting last_date to datetime object
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    year = last_date.year
    month = last_date.month

    # Depending on the month of the measure I need to determine if leap-year calculations are done on the current or previous year
    if month < 2:
        year -=1

    # Leap-year computing
    leap = False
    if last_date.year % 4 == 0 and \
    (last_date.year % 100 != 0 or last_date.year % 400 == 0):
        leap = True

    days = 365
    if leap == True:
        days = 366

    # Finding the most active station
    active_sta = session.query(Measurement.station, func.count(Measurement.date).label('count'))\
    .group_by(Measurement.station)\
    .order_by(desc('count'))
    first_station = active_sta[0][0]

    # Building the query
    hist_data = session.query(Measurement.station, Measurement.date, Measurement.tobs)\
    .filter(Measurement.station ==  first_station)\
    .limit(days)
    session.close()

    # Building the list
    station_temp = []
    for _ in hist_data:
        station_temp.append(_)

    # List of stations
    return jsonify(station_temp)
    
@app.route("/api/v1.0/<start>")
def date_start(start):
    # Building the query
    first =session.query(Measurement.date,\
        func.max(Measurement.tobs),\
        func.min(Measurement.tobs),\
        func.avg(Measurement.tobs))\
        .group_by(Measurement.date)\
        .filter(Measurement.date >= start)
    session.close()

    # Building the list
    start_list = []
    for _ in first:
        start_list.append(_)

    # List of temperatures stats
    return jsonify(start_list)
 
@app.route("/api/v1.0/<start>/<end>")
def date_start_end_query(start, end):

    # Building the query
    first =session.query(Measurement.date,\
            func.max(Measurement.tobs),\
            func.min(Measurement.tobs),\
            func.avg(Measurement.tobs))\
            .group_by(Measurement.date)\
            .filter(Measurement.date >= start,
                    Measurement.date <= end)

    # Building the list
    start_list = []
    for _ in first:
        start_list.append(_)

    # List of temperatures stats
    return jsonify(start_list)

if __name__ == "__main__":
    app.run(debug=True)

