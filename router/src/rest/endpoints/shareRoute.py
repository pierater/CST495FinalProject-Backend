#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Description: Rest endpoint for sharing routes between friends
Author: Pearce Reinsch
'''

shareRouteBlueprint = Blueprint('router', __name__, template_folder='templates')
@shareRouteBlueprint.route("/shareRoute/", methods=['POST'])
# takes a user's Id and desired Route and stores the share and route on the remote DB
# returns a success/failed response
def shareRoute(meId = None, youId = None, route = None, routeId = None, routeName = None, startLatitude = None, startLongitude = None):
	query = "INSERT INTO shared(toId, fromId, routeId) VALUES(%s,%s,%s)"

	if(meId is None):
		meId = request.json['meId']
		youId = request.json['youId']
		route = request.json['route']
		routeId = request.json['routeId']
		routeName = request.json['routeName']
		startLatitude = request.json['startLatitude']
		startLongitude = request.json['startLongitude']
		
	args = (youId, meId, routeId)
	try:
		dbconnect.__change_data(query,args)
		dbconnect.insert_data_routes(route,startLatitue,startLongitude,meId,routeName)
		return json.dumps(codes.SUCCESS)
	except Exception as e:
		return json.dumps(codes.FAILURE)