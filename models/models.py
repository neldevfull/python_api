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


# if __name__ == '__main__':
#     user_one = Users()
#     user_one.name = 'John Deer'
#     user_one.email = 'john@example.com'
#     user_one.save()

#     user_two = Users()
#     user_two.name = 'Mary Jane'
#     user_two.email = 'mary@example.com'
#     user_two.save()

#     print('Users successfully registered')

#     group = Groups()
#     group.name = 'Software Developers'
#     group.members.append(user_one)
#     group.members.append(user_two)
#     group.save()

#     print('Group successfully registered')