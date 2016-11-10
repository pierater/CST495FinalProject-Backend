#!/usr/bin/env python3.5
from. import preTest
import uploadRoute
import dbconnect
import codes
import json

'''
Author: Angel Soriano
Description: a test to test uploadRoute
'''
#test Data to insert into route
userID = "123"
startingPointLat = "36.733"
startingPointLon = "-125.666"
routeName = "coolRoute"
path = '{"lat" : [123, 456, 102, 004, 123], "lon" : [11, 33, 44, 55, 16] }'


def test_uploadRoute():

    # Inserting into database and getting a correct response
    response = uploadRoute.uploadRoute(userID, startingPointLat, startingPointLon, routeName, path)

    assert (json.loads(response).get('idroutes') != -1)

def test_badUpload():
    # Inserting bad values into the upload route so it fails
    response = uploadRoute.uploadRoute(userID, startingPointLat, startingPointLon,None, None)
    assert (response == codes.JSON_FAILURE)
'''
def test_routeUploaded():

    query = "SELECT * FROM 'routes' WHERE 'userid` = %s"
    try:
        cursor = dbconnect.__change_data(query, (userID, routeName))
    except:
'''

def teardown_function():
    # delete everything inserted into the database
    dbconnect.delete_data('routes', 'userid', userID)
