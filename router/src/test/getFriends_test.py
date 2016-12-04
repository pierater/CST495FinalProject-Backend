#!/usr/bin/env python3.4
from . import preTest
import getFriends
import createUser
import addFriend
import processRequest
import dbconnect
import codes
import json

'''
Author: Martin Almaraz
Description: Tests that we get the friends we expect
'''

class TestGetFriends_endpoint():

    user_id = None
    user_bio = 'bio0'
    user_username = 'user0'
    user_email = 'email0'
    user_privacy = 'PRIVATE'

    friend_id_1 = None
    friend_bio_1 = 'bio1'
    friend_username_1 = 'user1'
    friend_email_1 = 'email1'
    friend_privacy_1 = 'PRIVATE'

    friend_id_2 = None
    friend_bio_2 = 'bio2'
    friend_username_2 = 'user2'
    friend_email_2 = 'email2'
    friend_privacy_2 = 'PRIVATE'

    def test_getFriends_multiple(self):
        data = json.loads(getFriends.getFriends(self.user_id))

        assert len(data) == 2
    def test_get_zero_friends(self):
        self.teardown_method()
        
        data = json.loads(getFriends.getFriends(self.user_id))

        assert len((data)) == 0

    def setup_method(self):
        temp = json.loads(createUser.createUser(self.user_username, 'pass', self.user_bio, self.user_bio, self.user_privacy))['userId']

        if temp == -1:
            return
        else:
            self.user_id = temp

        self.friend_id_1 = json.loads(createUser.createUser(self.friend_username_1, 'pass', self.friend_bio_1, self.friend_email_1, self.friend_privacy_1))['userId']

        self.friend_id_2 = json.loads(createUser.createUser(self.friend_username_2, 'pass', self.friend_bio_2, self.friend_email_2, self.friend_privacy_2))['userId']

        addFriend.addFriend(self.friend_id_1, self.user_id)
        addFriend.addFriend(self.friend_id_2, self.user_id)

        processRequest.processRequest(self.user_id, self.friend_id_1, "YES")
        processRequest.processRequest(self.user_id, self.friend_id_2, "YES")


    def teardown_method(self):
        dbconnect.delete_data('users', 'idusers', self.friend_id_1)
        dbconnect.delete_data('users', 'idusers', self.friend_id_2)
        dbconnect.delete_data('users', 'idusers', self.user_id)

        dbconnect.delete_data('friend', 'user_id', self.user_id)
        dbconnect.delete_data('friend', 'user_id', self.friend_id_1)
        dbconnect.delete_data('friend', 'user_id', self.friend_id_2)

        dbconnect.delete_data('request', 'receiver_id', self.user_id)


