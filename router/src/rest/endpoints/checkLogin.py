#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
from codes import SUCCESS, FAILURE

'''
Description: Rest endpoint for checking login
Author: Martin Almaraz
'''

checkLoginBlueprint = Blueprint('checkLogin', __name__, template_folder='templates')
@checkLoginBlueprint.route("/checkLogin/", methods=['POST'])
def checkLogin(username = None, password = None):

    if username is None:
        username = request.json['username']
        password = request.json['password']

    query = "SELECT `username`, `pass` FROM `users` WHERE `username` = %s AND `pass` = %s"

    cursor = dbconnect.__change_data(query, (username, password))
    try:
        for key, value in (dict(cursor)).items():
            return json.dumps(SUCCESS)
        return json.dumps(FAILURE)
    except Exception as e:
        return json.dumps(FAILURE)
