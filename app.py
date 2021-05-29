# Libraries and dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
    )
    

@app.route("/api/v1.0/stations")
def stations():
    # Creating the query
    stations = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation)

    # Building the list
    sta_list = []
    for _ in stations:
        sta_list.append(_)

    # List of stations
    return jsonify(sta_list)


@app.route("/api/v1.0/tobs")
def tobs():
    return ""
#     - 
#         - Query the dates and temperature observations of the most active station for the last year of data.
#         - Return a JSON list of temperature observations (TOBS) for the previous year.

#     - /api/v1.0/<start> and /api/v1.0/<start>/<end>
#         - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#         - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#         - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

if __name__ == "__main__":
    app.run(debug=True)

