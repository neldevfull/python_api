# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from models.models import Users
import json

users   = Blueprint('users', __name__)
message = {'message': '', 'data': None}

@users.route('/users', methods=['GET'])
def get_users():
    users = json.loads(Users.objects.to_json())
    return jsonify({"users": users})

@users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    data = jsonify({'message': 'Search user %s' % id})
    return data

@users.route('/users', methods=['POST'])
def insert_users():
    try:
        users = request.get_json()
        user  = Users()

        for key in users.keys():
            setattr(user, key, users[key])

        user.save()

        message['message'] = 'User successfully registered'
        message['data']    = json.loads(user.to_json())

        return jsonify(message)
    except Exception as e:
        message['message'] = 'Failed to save User'
        message['data']    = e

        return jsonify(message)

@users.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    data = jsonify({'message': 'Update User %s!' % id})
    return data

@users.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    data = jsonify({'message': 'Delete User %s!' % id})
    return data