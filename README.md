# Hawaii Weather Data Analysis with Flask API

# Surfs Up! with Hawaii API v1.0

<img src="https://content.tripster.com/travelguide/wp-content/uploads/2017/09/Dropbox_abigail-lynn-316133-750x450.jpg">

## Background

To plan for a long holiday vacation in Honolulu, Hawaii, this project will do some climate analysis on the area.

## File Index

Following files are attached:

1. <a href="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/climate_starter.ipynb">climate_starter.ipynb</a>: Main notebook with bonus resolution.

2. <a href="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/app.py">app.py</a>: An flask app for ``Hawaii API v1.0``.

3. <a href="https://github.com/kk-deng/SQLAlchemy-Challenge/tree/main/Images">Images folder</a>: Four output images from notebook.

## Hawaii API App v1.0
### This API accepts the following functions:
* /api/v1.0/precipitation
   ``Return a JSON list of precipitation data for the last year in the database.``

* /api/v1.0/stations
  ``Return a JSON list of stations in the database.``

* /api/v1.0/tobs
  ``Return a JSON list of temperature observations (TOBS) of the most active station for the last year.``

* /api/v1.0/20170101
  ``Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date.``
  ``Start date must be in **YYYYMMDD** format.``

* /api/v1.0/20170101/20170801
  ``Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.``
  ``Start/end dates must be in **YYYYMMDD** format. And end date is later than start date.``

## Analysis

* A **paired test** was used to compare two related variables (Jun and Dec temperatues).
* In conclusion, from the p-value << 0.05, we can **reject the hypothesis** that June and Dec temperatues have no difference.

### Precipitation Analysis
<img width=800 src="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/Images/1.%20precipitation.png">

### Stations Histogram
<img width=800 src="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/Images/2.%20station.png">

### Trip Avg Temp
<img width=200 src="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/Images/3.%20trip%20avg%20temp.png">

### Daily Rainfall Average
<img width=800 src="https://github.com/kk-deng/SQLAlchemy-Challenge/blob/main/Images/4.%20daily%20rainfall%20avg.png">

