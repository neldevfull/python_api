# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, jsonify, request
from database.db import db_read, db_write

employees = Blueprint('employees', __name__)
response = {'message':''}

@employees.route('/employees/', methods=['POST'])
def insert_employee():
    data = request.get_json()
    db   = db_read()

    db['employees'].append(data)
    db_write(db)

    response['message'] = 'Employees %s successfully register' % data.get('name')
    return jsonify(response)

@employees.route('/employees/', methods=['GET'])
def get_all_employees():
    data = db_read()
    return jsonify(data)

@employees.route('/employees/<int:id>/', methods=['GET'])
def get_employee(id):
    data = db_read()

    for employee in data.get('employees'):
        if id == employee.get('id'):
            return jsonify(employee)

    response['message'] = 'Employee not found'
    return jsonify(response)
