from flask import Flask
from flask_cors import CORS
from .database.db import initialize_db


app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = "SECRET_KEY" 


app.config['MONGODB_SETTINGS'] = {
    "db": "deepawali",
    "host": "mongodb://mongo:CA5yXPtFhNLa9bgiTbj7@containers-us-west-58.railway.app:6245/deepawali",
    "username": "mongo",
    "password": "CA5yXPtFhNLa9bgiTbj7",
    "port": 6245
}

initialize_db(app)