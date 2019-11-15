#!/usr/bin/env python

from response import APIResponse
from flask import Flask, request
from firebase import Firebase

# initialize flask
app = Flask("kimhr-api")


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