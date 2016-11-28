#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect

'''
Description: Rest endpoint for retrieving nearby routes
Author: Pearce Reinsch
'''


getNearMeBlueprint = Blueprint('getNearMe', __name__, template_folder='templates')
@getNearMeBlueprint.route("/getNearMe/", methods=['POST'])
# takes a user's location (latitude & longitude) and a distance (in KM)
# returns a list of routes with a start point within the given distance of the user's location
def getNearMe(userLatitude = None, userLongitude = None, preferredDistance = None):
	isThisAProductionRun = userLatitude is None or userLongitude is None
	
	query = "SELECT idroutes, route, startPointLat, startPointLon, routeName, ( 3959 * acos( cos( radians(" + userLatitude
	query += " ) ) * cos( radians( startPointLat ) ) * cos( radians( startPointLon ) - radians(" + userLongitude
	query += " ) ) + sin( radians(" + userLatitude + ") ) * sin( radians( startPointLat ) ) ) ) "
	query += "AS distance FROM routes HAVING distance < " + str(preferredDistance) + " ORDER BY distance LIMIT 0 , 20" 

	try:
		assert (isThisAProductionRun == True)
	except AssertionError:
		userLatitude = request.json['userLat']
		userLongitude = request.json['userLon']
		preferredDistance = request.json['dist']
	finally:
		cursor = dbconnect.__change_data(query,preferredDistance)
		return json.dumps(cursor)
