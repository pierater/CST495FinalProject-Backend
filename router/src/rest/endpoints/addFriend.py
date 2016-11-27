#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconnect
import codes

'''
Author: Angel Soriano
Description: Endpoint to add a friend
'''

addFriendBlueprint = Blueprint('addFriend', __name__, template_folder='templates')
@addFriendBlueprint.route("/addFriend/", methods=['POST'])
def addFriend(user_id = None, friend_id = None):
    
    query = "INSERT INTO friend(user_id, friend_id) VALUES(%s,%s)"

    if user_id is None:
        payload = request.json
        user_id = payload["user_id"]
        friend_id = payload["friend_id"]
        
    args = (user_id, friend_id)

    try:
        dbconnect.__change_date(query, args)
        return codes.JSON_SUCCESS
    except:
        return codes.JSON_FAILURE
