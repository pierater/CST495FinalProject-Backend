from flask import Flask

app = Flask(__name__)



# EXAMPLE ROUTE
# Link to Docs: http://flask.pocoo.org/docs/0.11/
# to create a new endpoint you add @app.route('endpoint')
# then define it under it
@app.route("/hello")
def hello():
    return "Hello, World"
@app.route("/hello/<username>")
def show_user(username):
    return "Hello, %s" % username


# this line checks to see if the file was executed or imported
if __name__ == "__main__":
    app.run()
