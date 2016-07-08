#!/usr/bin/python

import requests
import json

headers  = {"Content-Type":"application/json"}
url_base = "http://192.168.33.11:5000/usuarios/"

# 200 Status OK
# print ("status " + str(requests.get(url_base).status_code))

# 404 Not Found
# print ("status " + str(requests.get("http://192.168.33.11:5000/usuarios/test/").status_code))

# List all users
def get_all_users():
    response = json.loads(requests.get(url_base)._content)

    print "List all users: "

    for res in response.get("usuarios"):
        print "id: " + str(res.get("id")) + " name: " + res.get("nome") + " " + " e-mail: " + res.get("email")

# Get for email
def get_for_email(email):
    response = json.loads(requests.get(url_base)._content)

    user_id = [user.get("id") for user in response.get("usuarios")
        if user.get("email") == email]

    return user_id

# Put user
def put_user(user_id, data):
    data = json.dumps(data)
    response = json.loads(requests.put("http://192.168.33.11:5000/usuarios/%s/" % user_id,
        data=data,
        headers=headers)
        ._content)

    return response

# Delete user
def delete_user(user_id):
    response = json.loads(requests.delete("http://192.168.33.11:5000/usuarios/%s/" % user_id,
        headers=headers)
        ._content)

    return response

# Post user
def post_user(data):
    user = get_for_email(data["email"])

    if user:
        print "E-mail already registered"
        return

    data  = json.dumps(data)
    response = json.loads(
            requests.post(url_base,
            data=data,
            headers=headers
            )._content)

    print response


if __name__ == "__main__":
    # post_user({"nome":"Joao Alcantra","email":"joao@alcantra.com"})
    # put_user(3, {"nome":"Jax Teller JR","email":"jax@gmail.com"})
    # delete_user(3)
    get_all_users()