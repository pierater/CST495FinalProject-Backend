#!/usr/bin/env python3.4
from . import preTest
import removeFriend, createUser
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
    
    #info for user2
    username2 = "testUser2"
    password2 = "pass2"
    bio2 = "No I'm Mr. Meeseeks look at me"

    #values for later
    user1 = 0
    user2 = 0

    def setup_function():
        # First have to create users
        user1 = json.loads(createUser.createUser(username1, password1, bio1))['userId']
        user2 = createUser.createUser(username2, password2, bio2)
        #make them friends
        dbconnect.__change_data()
