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

@dependents.route('/employees/<int:id>/dependents/<int:did>/', methods=['GET'])
def get_dependent(id, did):
    data = db_read()

    for employee in data.get('employees'):
        if id == employee.get('id'):
            for dependent in employee.get('dependents'):
                if did == dependent.get('id'):
                    return jsonify(dependent)

    response['message'] = 'Dependent not found'
    return jsonify(response)

@dependents.route('/employees/<int:id>/dependents/<int:did>/', methods=['DELETE'])
def delete_dependent(id, did):
    data = db_read()

    for employee in data.get('employees'):
        if id == employee.get('id'):
            for dependent in employee.get('dependents'):
                if did == dependent.get('id'):
                    employee.get('dependents').remove(dependent)
                    db_write(data)

                    response['message'] = 'Dependent successfully deleted'
                    return jsonify(response)

    response['message'] = 'Dependent not found'
    return jsonify(response)