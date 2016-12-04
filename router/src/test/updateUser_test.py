#!/usr/bin/env python3.5
from . import preTest
import createUser
import updateUser
from dbconnect import __change_data as change_data
import dbconnect
import json
import codes

'''
Author: Martin Almaraz
Description: A test that makes sure we can update a user
Updated: 2016-12-03
'''

class TestUpdateUser_endpoint():

    username = 'testuser'
    password = 's3cr3t'
    bio = 'this is a bio'
    email = 'email@mail.com'
    privacy = 'PRIVATE'

    def test_verify_updated_info(self):
        assert codes.JSON_SUCCESS == updateUser.updateUser(self.username, self.password, self.bio, self.privacy, self.userid, self.email)

        query = "SELECT * from `users` WHERE `idusers` = %s"
        args = (self.userid,)
        data = (change_data(query, args))
        print(data)
        data = data[0] 

        assert data['username'] == self.username
        assert data['bio'] == self.bio
        assert data['email'] == self.email
        assert data['privacy'] == self.privacy

    def setup_method(self):
        self.userid = json.loads(createUser.createUser(self.username, self.password, self.bio, self.email, self.privacy))['userId']
        self.username = 'newUsername'
        self.bio = 'newBio'
        self.email = 'newEmail'
        self.privacy = 'newPrivacy'

    def teardown_method(self):
        dbconnect.delete_data('users', 'idusers', self.userid)
