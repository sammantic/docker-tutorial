from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world, from the docker</p>"

app.run(host="0.0.0.0", port=5400)
