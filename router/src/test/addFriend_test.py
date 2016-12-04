#!/usr/bin/env python3.4
from . import preTest
import addFriend
import dbconnect
import json
import codes

'''
Author: Martin Almaraz
Description: Test for adding a addFriend
'''

user_id = 1
friend_id = 2

def test_addingFriend():
    assert addFriend.addFriend(user_id, friend_id) == codes.JSON_SUCCESS

def teardown_function():

    dbconnect.delete_data('request', 'receiver_id', friend_id)
    dbconnect.delete_data('request', 'sender_id', user_id)

