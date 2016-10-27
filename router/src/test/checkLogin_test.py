#!/usr/bin/env python3.4
from . import preTest
import checkLogin
import dbconnect
import codes

'''
Author: Martin Almaraz
Description: A test that tests checkLogin endpoint
'''


username = 'martin'
password = 'password'

def test_checkLogin():
    
    assert checkLogin.checkLogin(username, password) == codes.JSON_SUCCESS

def test_checkLogin_wrong_pass():

    assert checkLogin.checkLogin(username, 'badPass') == codes.JSON_FAILURE

def test_checkLogin_wrong_username():

    assert checkLogin.checkLogin('badUser', password) == codes.JSON_FAILURE

def setup_function():
    dbconnect.insert_data_users(username, "bio", password)

def teardown_function():
    dbconnect.delete_data('users', 'username', username)
