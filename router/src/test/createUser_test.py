#!/usr/bin/env python3.5
from . import preTest
import createUser
import dbconnect

'''
Author: Laura Chavez
Description: A test that tests createUser endpoint
'''


username = 'testuser'
password = 's3cr3t'
bio = 'this is a bio'
email = 'email@mail.com'

# Tests that a user can be created.
def test_createUser():
    userid = dbconnect.insert_data_users(username, bio, password, email)
    print (userid)
    assert userid is not None

# Test if username is already taken, user can't be created
def test_createExistingUser():
    dbconnect.insert_data_users(username, bio, password, email)
    userid = dbconnect.insert_data_users(username, bio, password, email)
    assert userid == -1

def teardown_function():
    dbconnect.delete_data('users', 'username', username)
