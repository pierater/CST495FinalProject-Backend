#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes
import logging

'''
Description: Rest endpoint for getting route shared with a user
Author: Pearce Reinsch
'''

getRoutesSharedBlueprint = Blueprint('getRoutesShared', __name__, template_folder='templates')
@getRoutesSharedBlueprint.route("/getRoutesShared/", methods=['POST'])
# takes a user's Id and searches for routes shared with them
# returns a dictionary of routes
def getRoutesShared(user_id = None):
	query = "SELECT route_name, route, start_point_lat, start_point_lon FROM `shared` WHERE `receiver_id` = %s"
	
	if(user_id is None):
		user_id = request.json['user_id']
		logging.info("getRoutesShared: " + str(payload))
	
	args = (user_id,)
	try:
		cursor = dbconnect.__change_data(query,args)
		return json.dumps(cursor)
	except Exception as e:
		logging.error("getRoutesShared: " + str(e))
		return json.dumps(codes.FAILURE)
