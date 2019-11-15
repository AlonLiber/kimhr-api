#!/usr/bin/env python

from flask import jsonify


class APIResponse(object):

    def __init__(self, data, status=200):
        """
        constructor
        """
        self.status = status
        self.data = data

    def make_response(self):
        """
        get response
        """
        return jsonify({
            "meta": {
                "status": self.status
            },

            "data": self.data
        })