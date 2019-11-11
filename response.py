#!/usr/bin/env python

from flask import jsonify, make_response


def make(data, status_code=200):
    """
    build success reponse
    """
    payload = jsonify({
        "data": data
    })

    r = make_response(payload)

    return r, status_code