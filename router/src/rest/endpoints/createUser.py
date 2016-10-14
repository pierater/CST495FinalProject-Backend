#!/usr/bin/env python3.5
import json
from flask import Blueprint, request
import dbconnect

'''
Description: Rest endpoint for creating a user
Author: Laura Chavez
'''

createUserBlueprint = Blueprint('createUser', __name__, template_folder='templates')
@createUserBlueprint.route("/createUser/", methods=['POST'])
def createUser(username = None, password = None, bio = None):

    if username is None:
        username = request.form['username']
        password = request.form['password']
        bio = request.form['bio']
    userid = dbconnect.insert_data_users(username,bio,password)
    return json.dumps('{userid: %s}') % userid
