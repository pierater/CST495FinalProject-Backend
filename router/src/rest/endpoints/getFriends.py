#!/usr/bin/env python3.4
import json
from flask import Blueprint, request
import dbconnect
import codes

'''
Author: Martin Almaraz
Description: Endpoint to get all current friends for a single user
'''

getFriendsBlueprint = Blueprint('getFriends', __name__, template_folder='templates')
@getFriendsBlueprint.route("/getFriends/", methods=['POST'])
def getFriends(userId = None):

    if userId is None:
        userId = request.json['userId']

    query = '''SELECT `username`, `bio`, `idusers` FROM
            (SELECT * FROM `users` INNER JOIN `friend` on `friend`.`friend_id` = `users`.`idusers` WHERE user_id = %s) as t;'''

    cursor = dbconnect.__change_data(query, (userId,))

    try:
        friends = cursor
        return json.dumps(friends)
    except Exception as e:
        print(e)
        return codes.JSON_FAILURE
