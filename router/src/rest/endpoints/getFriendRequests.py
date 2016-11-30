#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Author: Martin Almaraz
Description: Endpoint to get a list of pending friend requests
            for the user
'''

getFriendRequestsBlueprint = Blueprint('getFriendRequests', __name__, template_folder='templates')
@getFriendRequestsBlueprint.route("/getFriendRequests/", methods=['POST'])
def getFriendRequests(userId = None):

    if userId is None:
        userId = request.json['user_id']

    query = '''SELECT `username`, `bio`, `idusers` FROM
                (SELECT * FROM `users` INNER JOIN `request` on `request`.`sender_id` = `users`.`idusers`
                WHERE `receiver_id` = %s) as t'''

    cursor = dbconnect.__change_data(query, (userId,))

    try:
        reqs = cursor
        return json.dumps(reqs)
    except Exception as e:
        print(e)
        return codes.JSON_FAILURE
