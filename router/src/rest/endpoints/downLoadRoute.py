#!/usr/bin/env python3.5
import json
from flask import Blueprint, request
import dbconnect

'''
Author: Martin Almaraz
Description: Endpoint to download a certain route based on routId
'''

downloadRouteBlueprint = Blueprint('downloadRoute', __name__, template_folder='templates')
@downloadRouteBlueprint.route("/downloadRoute/", methods=['POST'])
def downloadRoute(routeId = None):

    if routId is None:
        routId = request.form['routeId']

    query = "SELECT `route`, `startPointLat`, `startPointLon` FROM `routes` WHERE `idroutes` = %s"
    cursor = dbconnect.__change_data(query, (routId,))
    try:
        route = (dict(cursor))
        return json.dumps(route['route'])
    except:
        return json.dumps('{status: failure}')
