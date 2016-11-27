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
def removeFriend(me_id = None, you_id = None):
    if me_id is None:
        payload = request.json
        me_id = payload["me_id"]
        you_id = payload["you_id"]

    query = "DELETE  FROM friends WHERE me_id = %s AND you_id = %s"
    args = (me_id, you_id)
    try:
        # execute query
        dbconnect.__change_date(query, args)
        return codes.JSON_SUCCESS

    except:
        # return non succesful
        return codes.JSON_FAILURE
