from flask import Flask
import json

import flask

app = Flask(__name__)

@app.route("/")
def index():
    with open('index.json') as d:
        data = json.load(d)
    
    return flask.jsonify(data)

@app.route("/get")
def get():
    with open('get.json') as d:
        data = json.load(d)
    
    return flask.jsonify(data)

@app.route("/post", methods = ['POST'])
def post():
    with open('post.json') as d:
        data = json.load(d)
    
    return flask.jsonify(data)
