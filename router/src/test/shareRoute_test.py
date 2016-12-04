#!/usr/bin/env python3.5
from . import preTest
import shareRoute
import createUser
import dbconnect
import codes
import json

'''
Author: Laura Chavez
Description: Tests that a route is able to be shared
Last Update: 03 December, 2016
'''

class TestShareRoute_endpoint():

    user_id = None
    user_bio = 'bio0'
    user_username = 'user0'
    user_email = 'email0'
    user_privacy = 'PRIVATE'

    friend_id = None
    friend_bio = 'bio1'
    friend_username = 'user1'
    friend_email = 'email1'
    friend_privacy = 'PRIVATE'

    startingPointLat = "37.10"
    startingPointLon = "-121.20"
    routeName = "myroute"
    route_id = 121

    def setup_method(self):
        self.user_id = json.loads(createUser.createUser(self.user_username, 'pass', self.user_bio, self.user_bio, self.user_privacy))['userId']
        self.friend_id = json.loads(createUser.createUser(self.friend_username, 'pass', self.friend_bio, self.friend_email, self.friend_privacy))['userId']

    def test_shareSuccessful(self):
        #sender_id, receiver_id, route , route_id , routeName , startLatitude,
        response = shareRoute.shareRoute(self.user_id, self.friend_id, " ", self.route_id, self.routeName, self.startingPointLat, self.startingPointLon)
        assert (response == codes.JSON_SUCCESS)

    def teardown_method(self):
        dbconnect.delete_data('users', 'idusers', self.friend_id)
        dbconnect.delete_data('users', 'idusers', self.user_id)
