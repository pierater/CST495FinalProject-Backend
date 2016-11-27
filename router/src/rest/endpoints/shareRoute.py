#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Description: Rest endpoint for sharing routes between friends
Author: Pearce Reinsch
'''

<<<<<<< HEAD

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
=======
shareRouteBlueprint = Blueprint('router', __name__, template_folder='templates')
@shareRouteBlueprint.route("/shareRoute/", methods=['POST'])
# takes a user's Id and desired Route and stores the share and route on the remote DB
# returns a success/failed response
def shareRoute(sender_id = None, receiver_id = None, route = None, route_id = None, routeName = None, startLatitude = None, startLongitude = None):
	query = "INSERT INTO shared(receiver_id, sender_id, route_id) VALUES(%s,%s,%s)"

	if(meId is None):
		sender_id = request.json['sender_id']
		receiver_id = request.json['receiver_id']
		route = request.json['route']
		route_id = request.json['route_id']
		routeName = request.json['routeName']
		startLatitude = request.json['startLatitude']
		startLongitude = request.json['startLongitude']
		
	args = (receiver_id, sender_id, routeId)
	try:
		dbconnect.__change_data(query,args)
		dbconnect.insert_data_routes(route,startLatitue,startLongitude,sender_id,routeName)
		return json.dumps(codes.SUCCESS)
	except Exception as e:
		return json.dumps(codes.FAILURE)
>>>>>>> 6238ee8db728ef8d587fe1987cbe8d487767338e
