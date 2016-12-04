#!/usr/bin/env python3.5
from . import preTest
import processRequest
from dbconnect import __change_data as runQuery
import dbconnect
import json

'''
Description: test for processRequest api endpoint
Author: Pearce Reinsch
'''

class TestProcessRequest():
	userId = 123
	friendId = 789
	responseYes = "YES"
	responseNo = "NO"
	checkFriendQuery = "SELECT * FROM friend WHERE user_id = %s AND friend_id = %s"
	checkRequestQuery = "SELECT * FROM request WHERE receiver_id = %s"

	# demonstrates that when a user accepts a friend request, both users
	#  are inserted as friends in the friend DB table and the request is
	#  deleted from the request DB table
	def test_processRequestYes(self):
		processRequest.processRequest(self.userId, self.friendId, self.responseYes)
		friendTableArgs1 = (self.userId, self.friendId)
		friendTableArgs2 = (self.friendId, self.userId)
		friendTableResult1 = runQuery(self.checkFriendQuery, friendTableArgs1)
		friendTableResult2 = runQuery(self.checkFriendQuery, friendTableArgs2)
		requestTableArgs = (self.userId, self.friendId)
		requestTableResult = runQuery(self.checkRequestQuery, requestTableArgs)
		assert requestTableResult == None
		assert len(friendTableResult1) == 1
		assert len(friendTableResult2) == 1

	# demonstrates that when a user rejects a friend request, neither user
	#  is listed as a friend in the friend DB table and the request is
	#  deleted from the request DB table
	def test_processRequestNo(self):
		processRequest.processRequest(self.userId, self.friendId, self.responseNo)
		friendTableArgs1 = (self.userId, self.friendId)
		friendTableArgs2 = (self.friendId, self.userId)
		friendTableResult1 = runQuery(self.checkFriendQuery, friendTableArgs1)
		friendTableResult2 = runQuery(self.checkFriendQuery, friendTableArgs2)
		requestTableArgs = (self.userId, self.friendId)
		requestTableResult = runQuery(self.checkRequestQuery, requestTableArgs)
		assert requestTableResult == None
		assert len(friendTableResult1) == 0
		assert len(friendTableResult2) == 0

	def setup_method(self):
		insertQuery = "INSERT INTO request(receiver_id, sender_id) VALUES(%s,%s)"
		args = (self.friendId, self.userId)
		runQuery(insertQuery, args)

	def teardown_method(self):
		dbconnect.delete_data('request', 'sender_id', self.userId)
		deleteQuery = "DELETE FROM friend WHERE user_id = %s AND friend_id = %s"
		args1 = (self.userId, self.friendId)
		args2 = (self.friendId, self.userId)
		runQuery(deleteQuery, args1)
		runQuery(deleteQuery, args2)