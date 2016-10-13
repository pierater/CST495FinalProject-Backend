'''
#!/usr/bin/env python3.5

from ... import app
import unittest
Description: test for making sure flask is up and running
Author: Martin Almaraz

class flaskTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.app.test_client()
        
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.post('/')
        
        self.assertEqual(result.status_code, 200)
        return
'''
