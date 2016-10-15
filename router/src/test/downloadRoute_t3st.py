#!/usr/bin/env python3.5
from . import preTest
import downloadRoute
import dbconnect

'''
Author: Martin Almaraz
Description: Tests to verify that downLoadRoute endpoint works
'''

routeStr = '[test route]'
routeId = '0'
userId = '1'
startPointLat = '123'
startPointLon = '456'

def test_downloadRoute():
    correctResponse = '{"userid": "%s", "startPointLon": "%s", "startPointLat": "%s", "route": "%s", "idroutes": "%s"}' % (userId, startPointLon, startPointLat, routeStr, routeId)

    assert downloadRoute.downloadRoute(routeId) == correctResponse


def test_downloadRoute_bad_routeid():
    correctResponse = '"{status: failure}"'

    assert downloadRoute.downloadRoute('00') == correctResponse


def setup_function():
    routeId = dbconnect.insert_data_routes(routeStr, startPointLat, startPointLon, userId, 'NULL')

def teardown_function():
    dbconnect.delete_data('routes', 'idroutes', routeId)

