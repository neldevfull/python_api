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