# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from models.models import Users
import json

users   = Blueprint('users', __name__)
message = {}

@users.route('/users', methods=['GET'])
def get_users():
    users = json.loads(Users.objects.to_json())
    return jsonify({"users": users})

@users.route('/users/<id>', methods=['GET'])
def get_user(id):
    status = 200
    user   = Users.objects(id=id)

    if user:
        message['message'] = 'User successfully found'
        message['user'] = json.loads(user.to_json())
    else:
        message['message'] = 'User not found'
        message['user'] = None
        status = 404

    return jsonify(message), status

@users.route('/users', methods=['POST'])
def insert_users():
    status = 200

    try:
        users = request.get_json()
        user  = Users()

        for key in users.keys():
            setattr(user, key, users[key])

        user.save()

        message['message'] = 'User successfully registered'
        message['user'] = json.loads(user.to_json())

    except Exception as e:
        message['message'] = 'Failed to save User'
        message['error'] = e
        status = 500

    return jsonify(message), status

@users.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    data = jsonify({'message': 'Update User %s!' % id})
    return data

@users.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    status = 200

    try:
        user = Users.objects(id=id)

        if user:
            message['message'] = 'User successfully deleted'
            message['user'] = json.loads(user.to_json())

            user.delete()
        else:
            message['message'] = 'User not foud'
            message['user'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Failed to delete User'
        message['error'] = e
        status = 500

    return jsonify(message), status