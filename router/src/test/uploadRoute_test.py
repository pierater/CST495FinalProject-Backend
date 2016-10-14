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
    correctResponse = '"{satus: success}"'

    assert uploadRoute.uploadRoute(userID, startingPointLat, startingPointLon, routeName, path) == correctResponse
   
    '''
    query = "SELECT * FROM 'routes' WHERE 'userid` = %s AND `routeName` = %s"
    try:
        cursor = dbconnect.__change_data(query, (userID, routeName))
    except:
        return 
    '''

