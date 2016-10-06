#!/bin/python3.5
import json
from flask import Blueprint

'''
Description: Rest endpoint for checking login
Author: Martin Almaraz
'''


checkLoginBlueprint = Blueprint('router', __name__, template_folder='templates')
@checkLoginBlueprint.route("/checkLogin")
def checkLogin(payload):
    payload = json.dumps(payload)
    username = payload['username']
    password = payload['password']
    
    query = "SELECT `password` FROM `USERS` WHERE `username` = %s AND `password` = %s" % (username, password)

    values = json.loads(dbUtil.runQuery(query))

    for key, value in values:
        if value == password:
            return json.loads('{status: success}')
    return json.loads('{status: failure}')

