import json

'''
Description: Rest endpoint for checking login
Author: Martin Almaraz
'''

@app.route("/checkLogin<username><password>")
def checkLogin(username, password):
    json_data = json.dumps({})

