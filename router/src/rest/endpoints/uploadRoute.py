#!/usr/bin/env python3.5
from flask import json
from flask import Blueprint
from flask import request

'''
Description: Rest endpoint for uploading route
Author: Angel Soriano`
'''

uploadRouteBlueprint = Blueprint('uploader', __name__, template_folder='templates')
@uploadRouteBlueprint.route("/uploadRoute/", methods=['POST'])
def uploadRoute():
    #Getting payload
    payload = request.json
    print(payload)

    # Getting all the values to insert into payload
    routeID = payload['id']
    startingPointLat = payload['route']['startingPoint']['lat']
    startingPointLon = payload['route']['startingPoint']['lon']
    routeName = payload['route']['name']
    path = payload['route']['path']

    print("RouteID:" + str(routeID))
    print("Starting point: Lat:%s Lon: %s" % ( str(startingPointLat), str(startingPointLon)))
    print("Route Name: " + str(routeName))
    print("Path: " + str(path))

    

    return json.dumps(request.json)
