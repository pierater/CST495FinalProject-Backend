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
def processRequest(meId = None, youId = None, response = None):
	query = "INSERT INTO friends(meId, youId) VALUES(%s,%s)"
	
	if(meId is None):
		meId = request.json['meId']
		youId = request.json['youId']
		response = request.json['response']
	
	response = response.lower()
	args = (meId, youId)
	if(response == codes.YES):
		try:
			dbconnect.__change_data(query,args)
			return json.dumps(codes.SUCCESS)
		except Exception as e:
			return json.dumps(codes.FAILURE)