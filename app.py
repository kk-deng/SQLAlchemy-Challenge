# =========== Import Dependencies ===========
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify


#SQLAlchemy 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Get last date and the most active station
session = Session(engine)
record = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc()).first()
max_date = dt.date.fromisoformat(record[0])
one_year = dt.timedelta(days = 365)
min_date = max_date - one_year

active_station = session.query(Measurement.station, func.count(Measurement.station))\
    .group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()
session.close()

#Flask 
app = Flask(__name__)
@app.route("/")
def main():    
    return (
        '<h1>Welcome to Hawaii API!</h1><br>\
        <h2>This API accepts the following functions:</h2><br>\
        <ul><li><a href="/api/v1.0/precipitation" target="_blank">/api/v1.0/precipitation</a><br>\
        Return a JSON list of precipitation data for the <b>last year</b> in the database.</li><br>\
        <li><a href="/api/v1.0/stations" target="_blank">/api/v1.0/stations</a><br>\
        Return a JSON list of <b>stations</b> in the database.</li><br>\
        <li><a href="/api/v1.0/tobs" target="_blank">/api/v1.0/tobs</a><br>\
        Return a JSON list of temperature observations (TOBS) of the most active station for the last year.</li><br>\
        <li><a href="/api/v1.0/20170101" target="_blank">/api/v1.0/<b>20170101</b></a><br>\
        Return a JSON list of the <b>minimum temperature</b>, the <b>average temperature</b>, and the <b>max temperature</b> for a given start date.<br>\
        Start date must be in <b>YYYYMMDD</b> format.</li><br>\
        <li><a href="/api/v1.0/20170101/20170801" target="_blank">/api/v1.0/<b>20170101</b>/<b>20170801</b></a><br>\
        Return a JSON list of the <b>minimum temperature</b>, the <b>average temperature</b>, and the <b>max temperature</b> for a given start-end range.<br>\
        Start date must be in <b>YYYYMMDD</b> format.</li><br>'
    )

@app.route("/api/v1.0/precipitation")
def prcp_route(): 
    session = Session(engine)
    results_1 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= min_date).all()
    session.close()
    return jsonify(dict(results_1))

@app.route("/api/v1.0/stations")
def station_route(): 
    session = Session(engine)
    # results = session.query(Measurement.station).group_by(Measurement.station).all()
    results_2 = session.query(Station.station, Station.name).all()
    session.close()
    return jsonify(dict(results_2))

@app.route("/api/v1.0/tobs")
def tobs_route(): 
    session = Session(engine)
    results_3 = session.query(Measurement.date, Measurement.tobs).filter_by(station = active_station[0]).filter(Measurement.date >= min_date).all()
    session.close()
    return jsonify(dict(results_3))

@app.route("/api/v1.0/<start>")
def start_route(start): 
    session = Session(engine)
    start_date = start[:4] + "-" + start[4:6] + "-" + start[-2:]
    results_4 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    session.close()
    return jsonify(
        TMin=results_4[0][0],
        TAvg=results_4[0][1],
        TMax=results_4[0][2]
    )

@app.route("/api/v1.0/<start>/<end>")
def start_end_route(start, end): 
    session = Session(engine)
    if start >= end:
        return (
            "<h2>Error: Invalid date range!</h2><br>\
            Please make sure the <b>end date(" + end + ")</b> is later than <b>start date(" + start +")</b>."
        )
    else:
        start_date = start[:4] + "-" + start[4:6] + "-" + start[-2:]
        end_date = end[:4] + "-" + end[4:6] + "-" + end[-2:]
        results_5 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
        session.close()
        return jsonify(
            TMin=results_5[0][0],
            TAvg=results_5[0][1],
            TMax=results_5[0][2]
        )

if __name__ == '__main__': 
    app.run(debug=True)
