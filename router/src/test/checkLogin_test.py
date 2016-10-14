#!/usr/bin/env python3.5
from . import preTest
import checkLogin
def test_checkLogin():
    correctResponse = '"{status: success}"'
    username = 'martin'
    password = 'password'
    
    assert checkLogin.checkLogin(username, password) == correctResponse
