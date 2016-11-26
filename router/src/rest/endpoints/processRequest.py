#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Description: Rest endpoint for processing a friend request
Author: Pearce Reinsch
'''

processRequestBlueprint = Blueprint('router', __name__, template_folder='templates')
@processRequestBlueprint.route("/processRequest/", methods=['POST'])
# takes the Ids of the users of the request and the response
# returns a success/failure response
def processRequest(user_id = None, friend_id = None, response = None):
	query = "INSERT INTO friend(user_id, friend_id) VALUES(%s,%s)"
	
	if(user_id is None):
		user_id = request.json['user_id']
		friend_id = request.json['friend_id']
		response = request.json['response']
	
	response = response.lower()
	args = (user_id, friend_id)
	if(response == codes.YES):
		try:
			dbconnect.__change_data(query,args)
			return json.dumps(codes.SUCCESS)
		except Exception as e:
			return json.dumps(codes.FAILURE)