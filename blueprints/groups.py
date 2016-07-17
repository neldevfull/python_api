# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from models.models import Users, Groups
import json

groups = Blueprint('groups', __name__)
message = {}

@groups.route('/groups', methods=['GET'])
def get_all_groups():
    groups = json.loads(Groups.objects.to_json())
    message['groups'] = groups

    return jsonify(message)

@groups.route('/groups/<id>', methods=['GET'])
def get_group(id):
    status = 200

    try:
        group = Groups.objects(id=id).first()

        if group:
            message['message'] = 'Group successfully found'
            message['group'] = json.loads(group.to_json())
        else:
            message['message'] = 'Group not found'
            message['group'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Error inserting group'
        message['error'] = e
        status = 500

    return jsonify(message), status


@groups.route('/groups', methods=['POST'])
def insert_group():
    status = 200

    try:
        user  = None
        group = Groups()
        data  = request.get_json()

        group.name = data['name']

        for u in data.get('members'):
            user = Users()
            for key in u.keys():
                setattr(user, key, u[key])
            user.save()
            group.members.append(user)

        group.save()

        message['message'] = 'Group successfuly registered'
        message['group'] = json.loads(group.to_json())

    except Exception as e:
        message['message'] = 'Error inserting group'
        message['error'] = e
        status = 500

    return jsonify(message), status

@groups.route('/groups/<id>', methods=['DELETE'])
def delete_group(id):
    status = 200

    try:
        group = Groups.objects(id=id)

        if group:
            message['message'] = 'Group successfully deleted'
            message['group'] = json.loads(group.to_json())

            group.delete()
        else:
            message['message'] = 'Group not found'
            message['group'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Error delete group'
        message['error'] = e
        status = 500

    return jsonify(message), status

@groups.route('/groups/<id>', methods=['PUT'])
def update_group(id):
    status = 200

    try:
        user  = None
        group = Groups.objects(id=id).first()
        data  = request.get_json()

        if group:
            group.name = data.get('name')

            for u in data.get('members'):
                user = Users.objects(id=u.get('id')).first()
                user.name = u.get('name')
                user.email = u.get('email')
                user.save()

                for item in group.members:
                    if user == item:
                        item = json.loads(user.to_json())

            group.save()

            message['message'] = 'Group successfully updated'
            message['group'] = json.loads(group.to_json())

        else:
            message['message'] = 'Group not found'
            message['group'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Error delete group'
        message['error'] = e
        status = 500

    return jsonify(message), status

@groups.route('/groups/<id>/members', methods=['POST'])
def insert_member(id):
    status = 200

    try:
        group  = Groups.objects(id=id).first()
        data   = request.get_json()
        member = Users()

        if group:
            for key in data.keys():
                setattr(member, key, data[key])

            member.save()
            group.members.append(member)
            group.save()

            message['message'] = 'Member successfully registered'
            message['error'] = json.loads(member.to_json())
        else:
            message['message'] = 'Group not found'
            message['group'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Error insert member'
        message['error'] = e
        status = 500

    return jsonify(message), status

@groups.route('/groups/<id>/members/<email>', methods=['DELETE'])
def delete_member(id, email):
    status = 200

    try:
        group  = Groups.objects(id=id).first()
        member = Users.objects(email=email).first()

        if group and member:
            group.members.remove(member)
            group.save()

            message['message'] = 'Member successfully deleted'
            message['error'] = json.loads(member.to_json())
        else:
            message['message'] = 'Group or Member not found'
            message['group'] = None
            status = 404

    except Exception as e:
        message['message'] = 'Error delete member'
        message['error'] = e
        status = 500

    return jsonify(message), status