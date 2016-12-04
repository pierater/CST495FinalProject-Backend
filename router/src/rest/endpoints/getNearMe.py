#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

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
    if userLatitude is None or userLongitude is None:
        userLatitude = request.json['userLat']
        userLongitude = request.json['userLon']
        preferredDistance = request.json['dist']

    query = "SELECT idroutes, route, startPointLon, startPointLat, routeName, ( 3959 * acos( cos( radians(" + str(userLatitude)
    query += " ) ) * cos( radians( startPointLat ) ) * cos( radians( startPointLon ) - radians(" + str(userLongitude)
    query += " ) ) + sin( radians(" + str(userLatitude) + ") ) * sin( radians( startPointLat ) ) ) ) "
    query += "AS distance FROM routes HAVING distance < " + str(preferredDistance) + " ORDER BY distance LIMIT 0 , 20" 

    try:
        cursor = dbconnect.__change_data(query,preferredDistance)
        return json.dumps(cursor)
    except:
        return codes.JSON_FAILURE
