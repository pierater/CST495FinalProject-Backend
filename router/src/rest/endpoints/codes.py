#!/usr/bin/env python3.4
import json

SUCCESS = {}
SUCCESS['status'] = "success"

FAILURE = {}
FAILURE['status'] = "failure"

JSON_SUCCESS = json.dumps(SUCCESS)

JSON_FAILURE = json.dumps(FAILURE)
