#!/usr/bin/env python 3.4
from . import preTest
import getRoutesShared
import dbconnect
import json
import codes

'''
Author: Martin Almaraz
Description: Test for getting routes that have been shared with users
'''

user_id_yes = 1
user_id_no = 2
sender_id = 3
route_name = 'routeName1'
route = 'route1'
startLat = 'startLat'
startLon = 'startLon'

def test_get_a_shared_route():
    data = json.loads(getRoutesShared.getRoutesShared(user_id_yes))
    data = data[0]
    assert data['route_name'] == route_name
    assert data['route'] == route
    assert data['start_point_lat'] == startLat
    assert data['start_point_lon'] == startLon

def test_get_no_shared_routes():
    data = json.loads(getRoutesShared.getRoutesShared(user_id_no))

    assert len(data) == 0

def setup_function():
    query = "INSERT INTO `shared` (`receiver_id`, `sender_id`, `route_name`, `route`, `start_point_lat`, `start_point_lon`) VALUES (%s, %s, %s, %s, %s, %s)"
    args = (user_id_yes, sender_id, route_name, route, startLat, startLon)

    dbconnect.__change_data(query, args)

def teardown_function():

    dbconnect.delete_data('shared', 'sender_id', sender_id)
