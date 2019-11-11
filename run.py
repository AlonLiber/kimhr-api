#!/usr/bin/env python

from app import app
from firebase_admin import credentials

import os
import sys
import argparse
import firebase_admin


def get_parser():
    """
    configure and get parser
    """
    parser = argparse.ArgumentParser("kimhr-api")

    parser.add_argument("-d", "--debug", help="run in debug mode", default=False, action="store_true", required=False)
    parser.add_argument("-p", "--port", help="port number", default=5000, required=False)

    return parser

def firebase_init():
    """
    initialize firebase
    """
    firebase_admin.initialize_app(credentials.Certificate("firebase-key.json"), {
        "databaseURL": "https://kimhr-e96a3.firebaseio.com"
    })


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

        # initialize firebase
        firebase_init()

        app.run(**{
            "host": "0.0.0.0",
            "debug": args.debug,
            "port": args.port
        })

    except Exception as e:
        print(str(e))
