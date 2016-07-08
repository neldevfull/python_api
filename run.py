# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = jsonify({'message': 'Response in Flask'})
    return data

@app.route('/users', methods=['GET'])
def get_users():
    data = jsonify({'message': 'All users'})
    return data

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    data = jsonify({'message': 'Search user %s' % id})
    return data

@app.route('/users', methods=['POST'])
def insert_users():
    data = jsonify({'message': 'Insert User!'})
    return data

@app.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    data = jsonify({'message': 'Update User %s!' % id})
    return data

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    data = jsonify({'message': 'Delete User %s!' % id})
    return data

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8000
    )