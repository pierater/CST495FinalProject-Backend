#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect

'''
Description: Rest endpoint for sharing routes between friends
Author: Pearce Reinsch
'''


getNearMeBlueprint = Blueprint('router', __name__, template_folder='templates')
@getNearMeBlueprint.route("/shareRoute/", methods=['POST'])
# takes a user's Id and desired Route and stores the share and route on the remote DB
# returns a success/failed response
def getNearMe(meId = None, youId = None, route = None, routeId = None, routeName = None, startLatitude = None, startLongitude = None):
	meId = None, youId = None, route = None, routeName = None, startLatitue = None, startLongitude = None
	isThisAProductionRun = meId is None
	
	query = "INSERT INTO shared(toId, fromId, routeId) VALUES(%s,%s,%s)"

	try:
		assert (isThisAProductionRun == True)
	except AssertionError:
		meId = request.json['meId']
		youId = request.json['youId']
		route = request.json['route']
		routeId = request.json['routeId']
		routeName = request.json['routeName']
		startLatitude = request.json['startLatitude']
		startLongitude = request.json['startLongitude']
	finally:
		args = (youId, meId, routeId)
		try:
			dbconnect.__change_data(query,args)
			dbconnect.insert_data_routes(route,startLatitue,startLongitude,meId,routeName)
			return json.dumps(codes.SUCCESS)
		except Exception as e:
			return json.dumps(codes.FAILURE)