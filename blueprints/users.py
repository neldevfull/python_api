# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    data = jsonify({'message': 'All users'})
    return data

@users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    data = jsonify({'message': 'Search user %s' % id})
    return data

@users.route('/users', methods=['POST'])
def insert_users():
    data = jsonify({'message': 'Insert User!'})
    return data

@users.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    data = jsonify({'message': 'Update User %s!' % id})
    return data

@users.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    data = jsonify({'message': 'Delete User %s!' % id})
    return data