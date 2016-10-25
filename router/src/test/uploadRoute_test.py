#!/usr/bin/env python3.5
from. import preTest
import uploadRoute
import dbconnect

'''
Author: Angel Soriano
Description: a test to test uploadRoute
'''

userID = "123"
startingPointLat = "36.733"
startingPointLon = "-125.666"
routeName = "coolRoute"
path = '{"lat" : [123, 456, 102, 004, 123], "lon" : [11, 33, 44, 55, 16] }'

def test_uploadRoute():
    correctResponse = '"{status: success}"'

    response = uploadRoute.uploadRoute(userID, startingPointLat, startingPointLon, routeName, path)
    assert (response == correctResponse)

def test_badUpload():
    correctResponse = '"{status: failure}"'

    response = uploadRoute.uploadRoute(userID, startingPointLat, startingPointLon,None, None)
    assert (response == correctResponse)
'''
def test_routeUploaded():

    query = "SELECT * FROM 'routes' WHERE 'userid` = %s"
    try:
        cursor = dbconnect.__change_data(query, (userID, routeName))
    except:
'''

def teardown_function():
    dbconnect.delete_data('routes', 'userid', userID)
