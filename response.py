#!/usr/bin/env python

from flask import jsonify


class APIResponse(object):

    def __init__(self, data=None):
        """
        constructor
        """
        self.data = data

    def make_response(self, status=200):
        """
        make response
        """
        return jsonify({
            "meta": {
                "status": status
            },

            "data": self.data
        }), status

    def make_405(self):
        """
        make 405
        """
        return jsonify({
            "meta": {
                "status": 405
            },

            "error": {
                "message": "method not allowed"
            }
        }), 405

    def make_500(self):
        """
        make 500
        """
        return jsonify({
            "meta": {
                "status": 500
            },

            "error": {
                "message": "internal server error"
            }
        }), 500
