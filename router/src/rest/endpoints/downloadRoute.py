#!/usr/bin/env python3.5
import json
from flask import Blueprint, request
import dbconnect

'''
Author: Martin Almaraz
Description: Endpoint to download a certain route based on routId
'''

downloadRouteBlueprint = Blueprint('router', __name__, template_folder='templates')
@downloadRouteBlueprint.route("/downloadRoute/", methods=['POST'])
def downloadRoute(routeId = None):

    if routeId is None:
        routeId = request.form['routeId']

    query = "SELECT * FROM `routes` WHERE `idroutes` = %s"
    cursor = dbconnect.__change_data(query, (routeId,))
    try:
        route = cursor
        return json.dumps(route[0])
    except Exception as e:
        print(e)
        return json.dumps('{status: failure}')
