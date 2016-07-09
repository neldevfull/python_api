# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from blueprints.users import users
from blueprints.groups import groups
from blueprints.employees import employees

app = Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(groups)
app.register_blueprint(employees)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8000
    )