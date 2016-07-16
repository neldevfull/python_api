# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from models.models import Groups
import json

groups = Blueprint('groups', __name__)

@groups.route('/groups')
def list_groups():
    groups = json.loads(Groups.objects.to_json())
    return jsonify({"groups": groups})

@groups.route('/groups/<int:id>', methods=['GET'])
def get_group(id):
    data = jsonify({'message': 'Search group %s' % id})
    return data

@groups.route('/groups', methods=['POST'])
def insert_groups():
    data = jsonify({'message': 'Insert group!'})
    return data

@groups.route('/groups/<int:id>', methods=['PUT'])
def update_groups(id):
    data = jsonify({'message': 'Update group %s!' % id})
    return data

@groups.route('/groups/<int:id>', methods=['DELETE'])
def delete_groups(id):
    data = jsonify({'message': 'Delete group %s!' % id})
    return data