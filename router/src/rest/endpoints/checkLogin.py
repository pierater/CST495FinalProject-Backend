#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
from codes import SUCCESS, FAILURE, JSON_FAILURE
import logging

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
        logging.info("checkLogin: " + str(request.json))

    query = "SELECT `idusers`, `username`FROM `users` WHERE `username` = %s AND `pass` = %s"

    cursor = dbconnect.__change_data(query, (username, password))
    try:
        for key, value in (dict(cursor[0])).items():
            return json.dumps(cursor)
        return JSON_FAILURE
    except Exception as e:
        logging.error("checkLogin: " + str(e))
        return JSON_FAILURE
