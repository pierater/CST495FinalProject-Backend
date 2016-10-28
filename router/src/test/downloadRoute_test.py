#!/usr/bin/env python3.4
from . import preTest
import downloadRoute
import dbconnect
import json

'''
Author: Martin Almaraz
Description: Tests to verify that downLoadRoute endpoint works
'''

class TestdownloadRoute_endpoints():
	routeStr = '[test route]'
	routeId = '0'
	userId = '1'
	startPointLat = '123'
	startPointLon = '456'
	routeName = 'test route'

	def test_downloadRoute(self):
		response = json.loads(downloadRoute.downloadRoute(self.routeId))
		assert response['idroutes'] == self.routeId
		assert response['route'] == self.routeStr
		assert response['startPointLat'] == self.startPointLat
		assert response['startPointLon'] == self.startPointLon
		assert response['userid'] == self.userId
		assert response['routeName'] == self.routeName

	def test_downloadRoute_bad_routeid(self):
		correctResponse = '"{status: failure}"'
		assert downloadRoute.downloadRoute('00') == correctResponse

	def setup_method(self):
		try:
			self.routeId = dbconnect.insert_data_routes(self.routeStr, self.startPointLat, self.startPointLon, self.userId, self.routeName)
			self.routeId = self.routeId[0]['idroutes']
		except:
			self.routeId = dbconnect.insert_data_routes(self.routeStr, self.startPointLat, self.startPointLon, self.userId, self.routeName)
			print("Darn CircleCI")
			
	def teardown_method(self):
		dbconnect.delete_data('routes', 'userId', self.userId)

