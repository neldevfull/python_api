# -*- coding: utf-8 -*-

from flask import Flask
from flask_mongoengine import MongoEngine
import datetime

app = Flask(__name__)

# Config database
app.config['MONGODB_SETTINGS'] = {'db':'pythonapi_db'}
db = MongoEngine(app)


class Users(db.Document):
    name = db.StringField()
    email = db.StringField(unique=True)
    registered_in = db.DateTimeField(default=datetime.datetime.now())


class Groups(db.Document):
    name = db.StringField(unique=True)
    members = db.ListField()


if __name__ == '__main__':
    user = Users()
    user.name = 'John Deer'
    user.email = 'john@example.com'
    user.save()
    print('User successfully registered')