#!/usr/bin/env python3.4
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

def test_checkLogin_wrong_pass():
    correctResponse = '"{status: failure}"'

    assert checkLogin.checkLogin(username, 'badPass') == correctResponse

def test_checkLogin_wrong_username():
    correctResponse = '"{status: failure}"'

    assert checkLogin.checkLogin('badUser', password) == correctResponse

def setup_function():
    dbconnect.insert_data_users(username, "bio", password)

def teardown_function():
    dbconnect.delete_data('users', 'username', username)
