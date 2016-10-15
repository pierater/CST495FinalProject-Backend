#!/usr/bin/env python3.5
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

    def test_downloadRoute(self):
        
        response = json.loads(downloadRoute.downloadRoute(self.routeId))
        assert response['idroutes'] == self.routeId
        assert response['route'] == self.routeStr
        assert response['startPointLat'] == self.startPointLat
        assert response['startPointLon'] == self.startPointLon
        assert response['userid'] == self.userId

    def test_downloadRoute_bad_routeid(self):
        correctResponse = '"{status: failure}"'

        assert downloadRoute.downloadRoute('00') == correctResponse


    def setup_method(self):
        self.routeId = dbconnect.insert_data_routes(self.routeStr, self.startPointLat, self.startPointLon, self.userId)
        self.routeId = self.routeId[0]['idroutes']
        print("here", self.routeId)

    def teardown_method(self):
        dbconnect.delete_data('routes', 'idroutes', self.routeId)

