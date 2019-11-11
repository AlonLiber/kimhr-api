#!/usr/bin/env python

from db import companies
from db import positions
from db import questions
from flask import Flask, request

import response

# initialize flask
app = Flask("kimhr-api")


@app.route("/companies", defaults={"id_": None}, methods=["GET", "POST"])
@app.route("/companies/<string:id_>", methods=["GET", "PUT"])
def companies_(id_):
    """
    """
    if request.method == "POST":
        return response.make(
            companies.push(request.get_json())
        )

    elif request.method == "PUT":
        return response.make(
            companies.update(id_, request.get_json())
        )

    return response.make(
        companies.get(id_)
    )

@app.route("/positions", defaults={"id_": None}, methods=["GET", "POST"])
@app.route("/positions/<string:id_>", methods=["GET", "PUT"])
def positions_(id_):
    """
    """
    if request.method == "POST":
        return response.make(
            positions.push(request.get_json())
        )

    elif request.method == "PUT":
        return response.make(
            positions.update(id_, request.get_json())
        )

    return response.make(
        positions.get(id_)
    )

@app.route("/questions", defaults={"id_": None}, methods=["GET", "POST"])
@app.route("/questions/<string:id_>", methods=["GET", "PUT"])
def questions_(id_):
    """
    """
    if request.method == "POST":
        return response.make(
            questions.push(request.get_json())
        )

    elif request.method == "PUT":
        return response.make(
            questions.update(id_, request.get_json())
        )

    return response.make(
        questions.get(id_)
    )


def run(options):
    """
    run app
    """
    app.run(options)
