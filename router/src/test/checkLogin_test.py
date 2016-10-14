#!/usr/bin/env python3.5
from . import preTest
import checkLogin
import dbconnect

'''
Author: Martin Almaraz
Description: A test that tests checkLogin endpoint
'''


username = 'martin'
password = 'password'

def test_checkLogin():
    correctResponse = '"{status: success}"'
    
    assert checkLogin.checkLogin(username, password) == correctResponse

def setup_function(test_checkLogin):
    dbconnect.insert_data_users(username, "bio", password)

def teardown_function(test_checkLogin):
    dbconnect.delete_data('users', 'username', username)
