#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Author: Martin Almaraz
Description: Endpoint to get all current friends for a single user
'''

getFriendsBlueprint = Blueprint('router', __name__, template_folder='templates')
@getFriendsBlueprint.route("/getFriends/", methods=['POST'])
def getFriends(userId = None):

    if userId is None:
        userId = request.json['userId']

    query = '''SELECT `username`, `bio`, `userId` FROM 
    `friend` INNER JOIN `users` ON friend.`friend_id` = users.`idusers`
    AND friend.`user_id` = %s'''

    cursor = dbconnect.__change_data(query, (userId,))

    try:
        friends = cursor
        return json.dumps(friends)
    except Exception as e:
        print(e)
        return codes.JSON_FAILURE
