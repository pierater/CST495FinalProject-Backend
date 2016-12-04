#!/usr/bin/env python3.4
from flask import Blueprint, request, json
import dbconnect
import codes
import logging

'''
Author: Angel Soriano
Description: Endpoint to return all users matching a certain string
'''

searchFriendsBlueprint = Blueprint('searchFriends', __name__, template_folder='templates')
@searchFriendsBlueprint.route("/searchFriends/", methods=['POST'])
def searchFriends(username = None):
    if username is None:
        logging.info("searchFriends: " + str(request.json))
        payload = request.json
        username = payload['username']
    username = '%' + username + '%'
    
    query = "SELECT `username`, `bio`, `idusers` FROM `users` WHERE `username` LIKE %s AND `privacy` = 'PUBLIC'"
    
    try:
        cursor = dbconnect.__change_data(query, (username,))
        return json.dumps(cursor)
    except Exception as e:
        logging.error('searchFriends: ' + str(e))
        return codes.JSON_FAILURE
