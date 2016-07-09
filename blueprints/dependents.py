# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, jsonify, request
from database.db import db_read, db_write

dependents = Blueprint('dependents', __name__)
response = {'message':''}

@dependents.route('/employees/<int:id>/dependents/', methods=['GET'])
def get_all_dependents(id):
    dependents = None
    data = db_read()

    for employee in data.get('employees'):
        if id == employee.get('id'):
            dependents = employee.get('dependents')

    if dependents == None:
        response['message'] = 'Employee has no dependents'
        return jsonify(response)

    return jsonify(dependents)

@dependents.route('/employees/<int:id>/dependents/', methods=['POST'])
def insert_depedent(id):
    data = db_read()
    dependent = request.get_json()

    for employee in data.get('employees'):
        if id == employee.get('id'):
            employee.get('dependents').append(dependent)
            db_write(data)

            response['message'] = 'Dependent successfully registered'
            return jsonify(response)

    response['message'] = 'Employee not found'
    return jsonify(response)