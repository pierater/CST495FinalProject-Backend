#!/usr/bin/env python3.4
from flask import Flask
import sys

sys.path.append('.')
sys.path.append('./src')
sys.path.append('./src/rest')
sys.path.append('./src/rest/endpoints')
sys.path.append('./src/rest/dbUtil')

import checkLogin
import createUser
import updateUser

application = Flask(__name__)
application.register_blueprint(checkLogin.checkLoginBlueprint)
application.register_blueprint(createUser.createUserBlueprint)
application.register_blueprint(updateUser.updateUserBlueprint)
if __name__ == '__main__':
    application.run(debug=True)
