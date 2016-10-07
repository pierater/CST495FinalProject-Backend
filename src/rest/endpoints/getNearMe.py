#!/usr/bin/env python3.5
import json
from flask import Blueprint, request
from ..dbUtil import dbconnect

'''
Description: Rest endpoint for retrieving nearby routes
Author: Pearce Reinsch
'''


checkLoginBlueprint = Blueprint('router', __name__, template_folder='templates')
@checkLoginBlueprint.route("/getNearMe/", methods=['POST'])
# takes a user's location (latitude & longitude) and a distance (in KM)
# 	returns a list of routes with a start point within the given distance of the user's location
def getNearMe(userLat, userLon, dist):
	query =  "SELECT idroutes, route, ( 3959 * acos( cos( radians(" + userLat
	query += " ) ) * cos( radians( startPointLat ) ) * cos( radians( startPointLon ) - radians(" + userLon
	query += " ) ) + sin( radians(" + userLat + ") ) * sin( radians( startPointLat ) ) ) ) "
	query += "AS distance FROM routes HAVING distance < 25 ORDER BY distance LIMIT 0 , 20" 
	
	'''
	~ routes Table ~
	
	idroutes INT NOT NULL AUTO_INCREMENT, 
	route VARCHAR(1000) NOT NULL,
	startPointLat VARCHAR(10) NOT NULL,
	startPointLon VARCHAR(10) NOT NULL,
	userid VARCHAR(45) NOT NULL, 
	
	'''

    cursor = dbconnect.__change_data(query)
    
    return json.dumps(dict(cursor))