#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
'''
Description: Rest endpoint for checking login
Author: Martin Almaraz
'''


checkLoginBlueprint = Blueprint('checkLogin', __name__, template_folder='templates')
@checkLoginBlueprint.route("/checkLogin/", methods=['POST'])
def checkLogin(username = None, password = None):

    if username is None:
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
