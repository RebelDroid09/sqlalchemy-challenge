from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Routes available: /api/v1.0/precipitation, /api/v1.0/stations, /api/v1.0/tobs, /api/v1.0/<start>, and /api/v1.0/<start>/<end>"

@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'Precipitation' api call...")
    return "Printing precipitation data..."