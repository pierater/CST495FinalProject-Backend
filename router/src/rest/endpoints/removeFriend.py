#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconnect
import codes

'''
Author: Angel Soriano
Description: Endpoint to remove a friend
'''

removeFriendBlueprint = Blueprint('removeFriend', __name__, template_folder='templates')
@removeFriendBlueprint.route("/removeFriend/", methods=['POST'])
def removeFriend(user_id = None, user_id = None):
    if user_id is None:
        payload = request.json
        user_id = payload["user_id"]
        user_id = payload["user_id"]

    query = "DELETE  FROM friend WHERE user_id = %s AND friend_id = %s"
    args = (user_id, user_id)
    try:
        # execute query
        dbconnect.__change_date(query, args)
        return codes.JSON_SUCCESS

    except:
        # return non succesful
        return codes.JSON_FAILURE
