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
def addFriend(me_id = None, you_id = None):
    
    query = "INSERT %s, %s INTO friends"

    if me_id is None:
        payload = request.json
        me_id = payload["me_id"]
        you_id = payload["you_id"]
        
    args = (me_id, you_id)

    try:
        dbconnect.__change_date(query, args)
        return codes.JSON_SUCCESS
    except:
        return codes.JSON_FAILURE
