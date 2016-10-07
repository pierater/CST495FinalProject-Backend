#!/usr/bin/env python3.5
import json
from flask import Blueprint, request
import dbconnect
'''
Description: Rest endpoint for checking login
Author: Martin Almaraz
'''


checkLoginBlueprint = Blueprint('router', __name__, template_folder='templates')
@checkLoginBlueprint.route("/checkLogin/", methods=['POST'])
def checkLogin():

    username = request.form['username']
    password = request.form['password']

    query = "SELECT `username`, `pass` FROM `users` WHERE `username` = %s AND `pass` = %s"

    cursor = dbconnect.__change_data(query, (username, password))
    try:
        for key, value in (dict(cursor)).items():
            return json.dumps('{status: success}')
        return json.dumps('{status: failure}')
    except Exception as e:
        return json.dumps('{status: failure, error: %s}') % (str(e))
