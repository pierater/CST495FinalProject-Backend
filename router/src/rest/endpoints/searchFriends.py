#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconect
import codes

'''
Author: Angel Soriano
Description: Endpoint to return all users matching a certain string
'''

searchFriendsBlueprint = Blueprint('searchFriends', __name__, template_folder='templates')
@searchFriendsBlueprint.route("/searchFriends/", methods=['POST'])
def searchFriends(username = None):
    if username is None:
        payload = request.json
        username = payload['username']
# not done but I want to get remove and add friend up
    
    query = "SELECT * FROM users WHERE username LIKE %s"
    
    try:
        cursor = dbconect.__change_data(query, username)
        return json.dumps(cursor)
    except:
        return codes.JSON_FAILURE
