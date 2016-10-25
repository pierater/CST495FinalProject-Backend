#!/usr/bin/env python3.5
from flask import json, Blueprint, request
import dbconnect

'''
Description: Rest endpoint for uploading route
Author: Angel Soriano`
'''

uploadRouteBlueprint = Blueprint('uploader', __name__, template_folder='templates')
@uploadRouteBlueprint.route("/uploadRoute/", methods=['POST'])
def uploadRoute(userID = None, startingPointLat = None, startingPointLon = None, routeName = None, path = None):

    if userID is None: 
        #Getting payload
        payload = request.json
        print(payload)

        # Getting all the values to insert into payload
        userID = payload['id']
        startingPointLat = payload['route']['startingPoint']['lat']
        startingPointLon = payload['route']['startingPoint']['lon']
        routeName = payload['route']['name']
        path = payload['route']['path']

        if userID != None and startingPointLat != None and startingPointLon != None and routeName != None and path != None:

            try:
                dbconnect.insert_data_routes(json.dumps(path), startingPointLat, startingPointLon, userID, routeName)
                return json.dumps('{status: success}')
            except:
                return json.dumps('{status: failure}')
        else:
            return json.dumps('{status: failure}')
    else:
        
        if userID != None and startingPointLat != None and startingPointLon != None and routeName != None and path != None:

            try:
                dbconnect.insert_data_routes(path, startingPointLat, startingPointLon, userID, routeName)
                return json.dumps('{status: success}')
            except:
                return json.dumps('{status: failure}')
        else:
            return json.dumps('{status: failure}')

