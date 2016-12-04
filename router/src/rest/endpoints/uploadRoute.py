#!/usr/bin/env python3.5
from flask import json, Blueprint, request
import dbconnect
import codes
import sys
import logging

'''
Description: Rest endpoint for uploading route
Author: Angel Soriano`
'''

uploadRouteBlueprint = Blueprint('uploadeRoute', __name__, template_folder='templates')
@uploadRouteBlueprint.route("/uploadRoute/", methods=['POST'])
def uploadRoute(userID = None, startingPointLat = None, startingPointLon = None, routeName = None, path = None):

    if userID is None: 
        #Getting payload
        payload = request.json

        logging.info('uploadRoute: ' + str(payload))
        # Getting all the values to insert into payload
        userID = payload['userId']
        startingPointLat = payload['route']['startingPoint']['lat']
        startingPointLon = payload['route']['startingPoint']['lon']
        routeName = payload['route']['name']
        path = payload['route']['path']

        if userID != None and startingPointLat != None and startingPointLon != None and routeName != None and path != None:

            try:
                returnPayload = dbconnect.insert_data_routes(json.dumps(path), startingPointLat, startingPointLon, userID, routeName)
                if returnPayload == -1:
                    return json.dumps(codes.FAILURE)
                return json.dumps(returnPayload[0])
            except TypeError as e:
                logging.error('uploadRoute: ' + str(e))
                return json.dumps(codes.FAILURE)
        else:
            return json.dumps(codes.FAILURE)
    else:
        
        if userID != None and startingPointLat != None and startingPointLon != None and routeName != None and path != None:

            try:
                returnPayload = dbconnect.insert_data_routes(path, startingPointLat, startingPointLon, userID, routeName)
                if returnPayload == -1:
                    return json.dumps(codes.FAILURE)
                return json.dumps(returnPayload[0])
            except Exception as e:
                logging.error('uploadRoute: ' + str(e))
                return json.dumps(codes.FAILURE)
        else:
            return json.dumps(codes.FAILURE)

