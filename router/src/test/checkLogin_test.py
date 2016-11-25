#!/usr/bin/env python3.4
from . import preTest
import checkLogin
import dbconnect
import codes
import json

'''
Author: Martin Almaraz
Description: A test that tests checkLogin endpoint
Last Updated: 2016-11-07
'''


username = 'martin'
password = 'password'
bio = 'bio'
email = 'email'
def test_checkLogin():
    
    response = json.loads(checkLogin.checkLogin(username, password))
    response = response[0]
    assert response['username'] == username
    assert response['bio'] == bio
    assert response['email'] == email

def test_checkLogin_wrong_pass():

    assert checkLogin.checkLogin(username, 'badPass') == codes.JSON_FAILURE

def test_checkLogin_wrong_username():

    assert checkLogin.checkLogin('badUser', password) == codes.JSON_FAILURE

def setup_function():
    dbconnect.insert_data_users(username, bio, password, email)

def teardown_function():
    dbconnect.delete_data('users', 'username', username)
