#!/usr/bin/env python3.4
from flask import Flask
import sys

sys.path.append('.')
sys.path.append('./src')
sys.path.append('./src/rest')
sys.path.append('./src/rest/endpoints')
sys.path.append('./src/rest/dbUtil')

import checkLogin
import uploadRoute
import createUser
import downloadRoute
import getNearMe
import removeFriend
import addFriend

application = Flask(__name__)
application.register_blueprint(checkLogin.checkLoginBlueprint)
application.register_blueprint(createUser.createUserBlueprint)
application.register_blueprint(uploadRoute.uploadRouteBlueprint)
application.register_blueprint(downloadRoute.downloadRouteBlueprint)
application.register_blueprint(getNearMe.getNearMeBlueprint)
application.register_blueprint(removeFriend.removeFriendBlueprint)
application.register_blueprint(addFriend.addFriendBlueprint)


if __name__ == '__main__':
    application.run(debug=True)
