from flask import Flask
from flask_cors import CORS
from .database.db import initialize_db
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config.from_prefixed_env()
cors = CORS(app)

app.config['SECRET_KEY'] = app.config["SECRET_KEY"]


DB_URI = app.config["DB_URI"]
print(DB_URI)
app.config["MONGODB_HOST"] = DB_URI

initialize_db(app)
