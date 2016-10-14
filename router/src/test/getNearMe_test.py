#!/usr/bin/env python3.5
from ..rest.endpoints import getNearMe

'''
Description: test for getNearMe api endpoint
Author: Pearce Reinsch
'''

def test_getNearMe():
    userLat = "36.65"
    userLon = "-121.8"
    dist = "10"

