#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect

'''
Description: Rest endpoint for processing a friend request
Author: Pearce Reinsch
'''

processRequestBlueprint = Blueprint('router', __name__, template_folder='templates')
@processRequestBlueprint.route("/processRequest/", methods=['POST'])
# takes the Ids of the users of the request and the response
# returns a success/failure response
def processRequest(meId = None, youId = None, response = None):
	isThisAProductionRun = meId is None
	yesString = "yes"
	noString = "no"
	query = "INSERT INTO friends(meId, youId) VALUES(%s,%s)"

	try:
		assert (isThisAProductionRun == True)
	except AssertionError:
		meId = request.json['meId']
		youId = request.json['youId']
		response = request.json['response']
	finally:
		response = response.lower()
		args = (meId, youId)
		if(response == yesString):
			try:
				dbconnect.__change_data(query,args)
				return json.dumps(codes.SUCCESS)
			except Exception as e:
				return json.dumps(codes.FAILURE)