#!/usr/bin/env python3.5
from . import preTest
import createUser
import dbconnect

'''
Author: Laura Chavez
Description: A test that tests createUser endpoint
Updated: 7 November, 2016
'''

username = 'testuser'
password = 's3cr3t'
bio = 'this is a bio'
email = 'email@mail.com'

# Tests that a user can be created.
def test_createUser():
    userid = dbconnect.insert_data_users(username, bio, password, email)
    assert userid is not None


# Test if username is already taken, user can't be created
def test_createExistingUser():
    dbconnect.insert_data_users(username, bio, password, email)
    userid = dbconnect.insert_data_users(username, bio, password, email)
    assert userid == -1

# Test that user can still be created with empty bio
def test_createUserWithNoBio():
    emptyBio = ""
    userid = dbconnect.insert_data_users(username, emptyBio, password, email)
    assert userid is not None

def teardown_function():
    dbconnect.delete_data('users', 'username', username)
