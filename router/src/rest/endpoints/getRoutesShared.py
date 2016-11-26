#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect

'''
Description: Rest endpoint for getting route shared with a user
Author: Pearce Reinsch
'''

getRoutesSharedBlueprint = Blueprint('router', __name__, template_folder='templates')
@getRoutesSharedBlueprint.route("/getRoutesShared/", methods=['POST'])
# takes a user's Id and searches for routes shared with them
# returns a dictionary of routes
def getRoutesShared(meId = None):
	isThisAProductionRun = meId is None
	
	query = "SELECT routeId FROM shared WHERE toId = %s"
	args = (meID)

	try:
		assert (isThisAProductionRun == True)
	except AssertionError:
		meId = request.json['meId']
	finally:
		cursor = dbconnect.__change_data(query,args)
		routeIds = json.dumps(cursor)
		try:
			query2 = "SELECT route,routeName,startPointLat,startPointLon FROM routes WHERE routeId IN ("
			for key in routeIds:
				query2 += routeIds[key]
			query2 += ")"
			cursor2 = dbconnect.__change_data(query2,None)
			return json.dumps(cursor)
		except Exception as e:
			return json.dumps(codes.FAILURE)