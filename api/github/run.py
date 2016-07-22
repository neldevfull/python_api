# -*- coding: utf-8 -*-

import requests
import json
from my_token import get_token

user = 'neldevfull'
uri_base = 'https://api.github.com{}'

def user():
    response = requests.get(uri_base.format('/user'), auth=(user, get_token()))
    print(response.json())

if __name__ == '__main__':
    user()