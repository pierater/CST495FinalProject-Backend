#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import logging

'''
Description: Rest endpoint for creating a user
Author: Laura Chavez
'''

createUserBlueprint = Blueprint('createUser', __name__, template_folder='templates')
@createUserBlueprint.route("/createUser/", methods=['POST'])
def createUser(username = None, password = None, bio = None, email = None, privacy = None):

	if username is None:
		username = request.json['username']
		password = request.json['password']
		bio = request.json['bio']
		email = request.json['email']
		privacy = request.json['privacy']
		logging.info("createUser: " + str(request.json))
	
	try:
		userid = dbconnect.insert_data_users(username,bio,password,email,privacy)
		payload = {}
		payload['userId'] = userid
	except Exception as e:
		logging.error("createUser: " + str(e))
	
	return json.dumps(payload)