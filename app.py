#!/usr/bin/env python

from response import APIResponse
from flask import Flask, request
from firebase import Firebase
from firebase_admin import credentials

import os
import argparse
import firebase_admin
import sys
import json

# initialize flask
app = Flask("kimhr-api")

try:
    fk = json.load(open("firebase-key.json", "r"))

except:
    fk = {}

# initialize firebase
firebase_admin.initialize_app(credentials.Certificate({
        "type": fk.get("type") or os.environ.get("FK_TYPE"),
        "project_id": fk.get("project_id") or os.environ.get("FK_PROJECT_ID"),
        "private_key_id": fk.get("private_key_id") or os.environ.get("FK_PRIVATE_KEY_ID"),
        "private_key": fk.get("private_key") or os.environ.get("FK_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": fk.get("client_email") or os.environ.get("FK_CLIENT_EMAIL"),
        "client_id": fk.get("client_id") or os.environ.get("FK_CLIENT_ID"),
        "auth_uri": fk.get("auth_uri") or os.environ.get("FK_AUTH_URI"),
        "token_uri": fk.get("token_uri") or os.environ.get("FK_TOKEN_URI"),
        "auth_provider_x509_cert_url": fk.get("auth_provider_x509_cert_url") or os.environ.get("FK_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": fk.get("client_x509_cert_url") or os.environ.get("FK_CLIENT_X509_CERT_URL")
    }), {
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

if __name__ == "__main__":
    """
    main function
    """
    try:
        os.environ["FLASK_ENV"] = "development"

        app.run(**{
            "host": "0.0.0.0",
            "port": 5000,
            "debug": True
        })

    except Exception as e:
        print(str(e))

