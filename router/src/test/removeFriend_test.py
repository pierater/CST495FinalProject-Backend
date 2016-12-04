#!/usr/bin/env python3.4
from . import preTest
import removeFriend, createUser, addFriend, processRequest
import dbconnect
import codes
import json

'''
Author: Angel Soriano
Description: A test that removes a friend
'''

class TestRemoveFriend_endpoint():

    #info for user1
    username1 = "testUser1"
    password1 = "pass1"
    bio1 = "I'm Mr. Meeseeks look at me"
    email1 = "test1@email.com"
    privacy = "PUBLIC"
    #info for user2
    username2 = "testUser2"
    password2 = "pass2"
    bio2 = "No I'm Mr. Meeseeks look at me"
    email2 = "test2@email.com"
    #values for later
    user1 = 0
    user2 = 0
    user3 = 0

    def test_removeFriend(self):
        assert removeFriend.removeFriend(self.user1, self.user2) == codes.JSON_SUCCESS


    def setup_method(self):
        # First have to create users
        self.user1 = json.loads(createUser.createUser(self.username1, self.password1, self.bio1, self.email1, self.privacy))['userId']
        self.user2 = json.loads(createUser.createUser(self.username2, self.password2, self.bio2, self.email2, self.privacy))['userId']

        #make them friends
        addFriend.addFriend(self.user1, self.user2)
        processRequest.processRequest(self.user2, self.user1, codes.YES)

    def teardown_method(self):
        dbconnect.delete_data('users', 'idusers', self.user1)
        dbconnect.delete_data('users', 'idusers', self.user2)
