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
def getNearMe(userLat = None, userLon = None, dist = None):
	'''
	This query requires: 
	userLat (the user's latitude coordinate ie: 80.12)
	userLon (the user's longitude coordinate ie: -46.49)
	dist	(the user's preferred search distance in KM ie: 10)
	'''
	if userLat is None or userLon is None:
		userLat = request.json['userLat']
		userLon = request.json['userLon']
		dist = request.json['dist']

	query = "SELECT idroutes, route, ( 3959 * acos( cos( radians(" + userLat
	query += " ) ) * cos( radians( startPointLat ) ) * cos( radians( startPointLon ) - radians(" + userLon
	query += " ) ) + sin( radians(" + userLat + ") ) * sin( radians( startPointLat ) ) ) ) "
	query += "AS distance FROM routes HAVING distance < " + str(dist) + " ORDER BY distance LIMIT 0 , 20" 
	'''
	~ routes Table ~
	
	idroutes INT NOT NULL AUTO_INCREMENT, 
	route VARCHAR(1000) NOT NULL,
	startPointLat VARCHAR(10) NOT NULL,
	startPointLon VARCHAR(10) NOT NULL,
	userid VARCHAR(45) NOT NULL, 
	
	'''
	cursor = dbconnect.__change_data(query,dist)
	
	'''
	The returned object is structured as a list of JSON objects
	ie:
	
	[{'route': '***', 'idroutes': 50, 'distance': 1.488970881174448}, 
	{'route': '***', 'idroutes': 51, 'distance': 9648.624280895436}]
	
	this example has 2 route JSON objects with the accessible values being 
	'route' 'idroutes' and 'distance'
	
	these values are the actual route points, the id of the route, and the distance from the
	user's entered coordinates
	'''
	
	return json.dumps(cursor)
