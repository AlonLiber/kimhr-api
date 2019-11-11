#!/usr/bin/env python

from db import firebase
from firebase_admin import db

# firebase child
CHILD = "positions"


def push(value):
    """
    add position
    """
    return firebase.push(CHILD, value)

def get(id_):
    """
    get position/s
    """
    return firebase.get(CHILD, id_)

def update(id_, value):
    """
    update position
    """
    return firebase.update(CHILD, id_, value)