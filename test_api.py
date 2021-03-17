import pytest

import requests

import json

def main_url():
    return "https://reqres.in"


def test_valid_login():
    main_url2 = main_url()
    url = main_url2 + "/api/login/"

    data = {'email' :"eve.holt@reqres.in" , 'password' :'cityslicka'}
    response = requests.post(url,data=data)

    token = json.loads(response.text)


    assert response.status_code == 200

    assert token['token'] == "QpwL5tke4Pnpja7X4"


#to run use pytest test_api.py