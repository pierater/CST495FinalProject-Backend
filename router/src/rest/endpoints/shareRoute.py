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