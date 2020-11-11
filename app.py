import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite://Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurements = Base.classes.measurement
stations = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Routes available: /api/v1.0/precipitation, /api/v1.0/stations, /api/v1.0/tobs, /api/v1.0/<start>, and /api/v1.0/<start>/<end>"

@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'Precipitation' api call...")
    return "Printing precipitation data..."

@app.route("/api/v1.0/stations")
def getStations():
    print("Server received request for 'Stations' api call...")

    session = Session(engine)   

    results = session.query(stations.name).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def getStations():
    print("Server received request for 'Stations' api call...")

    session = Session(engine)   

    results = session.query(stations.name).all()

    session.close()

    all_names = list(np.ravel(results))

    return jsonify(all_names)

if __name__ == '__main__':
    app.run(debug=True)