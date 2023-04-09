from .db import db


class User(db.Document):
    user_name = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, unique=True)