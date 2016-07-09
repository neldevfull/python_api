# -*- coding: utf-8 -*-

import json

file  = 'db.json'

def db_write(data):
    with open(file, 'w') as f:
        f.write(json.dumps(data))

def db_read():
    with open(file, 'r') as f:
        return json.loads(f.read())