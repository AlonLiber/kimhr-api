#!/usr/bin/env python

from response import APIResponse
from flask import Flask, request
from firebase import Firebase
from firebase_admin import credentials

import os
import argparse
import firebase_admin
import sys

# initialize flask
app = Flask("kimhr-api")

firebase_admin.initialize_app(credentials.Certificate("firebase-key.json"), {
    "databaseURL": "https://kimhr-e96a3.firebaseio.com"
})

@app.errorhandler(405)
def make_405(e):
    """
    make 405
    """
    return APIResponse().make_405()

@app.errorhandler(500)
def make_500(e):
    """
    make 500
    """
    return APIResponse().make_500()

@app.route("/companies/<string:id_>", methods=["GET", "PUT"])
@app.route("/companies", methods=["GET", "POST"])
def companies(id_=None):
    """
    companies route
    """
    child = ("companies", "companies/%s" % (id_))[request.method == "PUT"]

    if request.method == "POST":
        data = Firebase(child).push(request.get_json())

    elif request.method == "PUT":
        data = Firebase(child).update(request.get_json())

    else:
        data = Firebase(child).get(id_)

    return APIResponse(data).make_response()

@app.route("/positions/<string:id_>", methods=["GET", "PUT"])
@app.route("/positions", methods=["GET", "POST"])
def positions(id_=None):
    """
    companies route
    """
    child = ("positions", "positions/%s" % (id_))[request.method == "PUT"]

    if request.method == "POST":
        data = Firebase(child).push(request.get_json())

    elif request.method == "PUT":
        data = Firebase(child).update(request.get_json())

    else:
        data = Firebase(child).get(id_)

    return APIResponse(data).make_response()

@app.route("/questions/<string:id_>", methods=["GET", "PUT"])
@app.route("/questions", methods=["GET", "POST"])
def questions(id_=None):
    """
    companies route
    """
    child = ("questions", "questions/%s" % (id_))[request.method == "PUT"]

    if request.method == "POST":
        data = Firebase(child).push(request.get_json())

    elif request.method == "PUT":
        data = Firebase(child).update(request.get_json())

    else:
        data = Firebase(child).get(id_)

    return APIResponse(data).make_response()

@app.route("/candidates/<string:id_>", methods=["GET", "PUT"])
@app.route("/candidates", methods=["GET", "POST"])
def candidates(id_=None):
    """
    companies route
    """
    child = ("candidates", "candidates/%s" % (id_))[request.method == "PUT"]

    if request.method == "POST":
        data = Firebase(child).push(request.get_json())

    elif request.method == "PUT":
        data = Firebase(child).update(request.get_json())

    else:
        data = Firebase(child).get(id_)

    return APIResponse(data).make_response()

@app.route("/answers/<string:id_>", methods=["GET", "PUT"])
@app.route("/answers", methods=["GET", "POST"])
def answers(id_=None):
    """
    companies route
    """
    child = ("answers", "answers/%s" % (id_))[request.method == "PUT"]

    if request.method == "POST":
        data = Firebase(child).push(request.get_json())

    elif request.method == "PUT":
        data = Firebase(child).update(request.get_json())

    else:
        data = Firebase(child).get(id_)

    return APIResponse(data).make_response()

def get_parser():
    """
    configure and get parser
    """
    parser = argparse.ArgumentParser("kimhr-api")

    parser.add_argument("-d", "--debug", help="run in debug mode", default=False, action="store_true", required=False)
    parser.add_argument("-p", "--port", help="port number", default=5000, required=False)

    return parser

if __name__ == "__main__":
    """
    main function
    """
    try:
        args = get_parser().parse_args()

        if args.debug == True:
            os.environ["FLASK_ENV"] = "development"

        else:
            os.environ["FLASK_ENV"] = "production"

        app.run(**{
            "host": "0.0.0.0",
            "debug": args.debug,
            "port": args.port
        })

    except Exception as e:
        print(str(e))