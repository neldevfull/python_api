# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

groups = Blueprint('groups', __name__)

@groups.route('/groups')
def list_groups():
    data = jsonify({'message': 'All groups!'})
    return data