#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Description: Rest endpoint for getting route shared with a user
Author: Pearce Reinsch
'''

getRoutesSharedBlueprint = Blueprint('getRoutesShared', __name__, template_folder='templates')
@getRoutesSharedBlueprint.route("/getRoutesShared/", methods=['POST'])
# takes a user's Id and searches for routes shared with them
# returns a dictionary of routes
def getRoutesShared(sender_id = None):
	query = '''SELECT * FROM (SELECT * FROM `routes` INNER JOIN `shared`
                    on `shared`.`route_id` = `routes`.`idroutes` WHERE `userid` = %s) as t'''
	
	if(sender_id is None):
		sender_id = request.json['user_id']
	
	args = (sender_id,)
	try:
		cursor = dbconnect.__change_data(query,args)
		return json.dumps(cursor)
	except Exception as e:
		print(e)
		return json.dumps(codes.FAILURE)
