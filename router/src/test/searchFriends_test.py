#!/usr/bin/env python3.4
from . import preTest
import searchFriends, createUser
import dbconnect
import codes
import json

'''
Author: Angel Soriano
Description: Tests the searchFriends endpoint
'''

class TestSearchFriends():
    
    # shared variables
    password = "life is endless stream of consciousness"
    bio = "do you think you're better off alone"
    privacy = "PUBLIC"

    # info for user1 
    username1 = "testuser1"
    email1 = "user1@email.com"

    # user2
    username2 = "testuser2"
    email2 = "user2@email.com"

    # user3
    username3 = "jerry"
    email3 = "jerry@email.com"

    # tracked variables
    user1 = 0
    user2 = 0
    jerry = 0
    
    def test_searchFriends(self):
        data = searchFriends.searchFriends("jerry")
        data = json.loads(data)
        print (data[0])
        assert len(list(data)) == 1
        assert "jerry" == data[0]['username']
        data = searchFriends.searchFriends("user")
        data = json.loads(data)
        assert len(data) == 2

    def test_bad_searchFreinds(self):
        data = searchFriends.searchFriends("meeeee")
        assert data == '[]'

    def setup_method(self):
        # Creating users
        self.user1 = json.loads(createUser.createUser(self.username1, self.password, self.bio, self.email1, self.privacy))['userId']
        self.user2 = json.loads(createUser.createUser(self.username2, self.password, self.bio, self.email2, self.privacy))['userId']
        self.jerry = json.loads(createUser.createUser(self.username3, self.password, self.bio, self.email3, self.privacy))['userId']

    def teardown_method(self):
        dbconnect.delete_data('users', 'idusers', self.user1)
        dbconnect.delete_data('users', 'idusers', self.user2)
        dbconnect.delete_data('users', 'idusers', self.jerry)
