#!/usr/bin/env python3.5
from flask import Flask
from src.rest.endpoints import checkLogin

app = Flask(__name__)
app.register_blueprint(checkLogin.checkLoginBlueprint)


if __name__ == "__main__":
    app.run()
