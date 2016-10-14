#!/usr/bin/env python3.5
from flask import Flask
import sys

sys.path.append('.')
sys.path.append('./src')
sys.path.append('./src/rest')
sys.path.append('./src/rest/endpoints')
sys.path.append('./src/rest/dbUtil')

import checkLogin
import uploadRoute

app = Flask(__name__)
app.register_blueprint(checkLogin.checkLoginBlueprint)
app.register_blueprint(uploadRoute.uploadRouteBlueprint)

app.run(debug=True)
