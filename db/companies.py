#!/usr/bin/env python

from db import firebase
from firebase_admin import db

# firebase child
CHILD = "companies"


def push(value):
    """
    add company
    """
    return firebase.push(CHILD, value)

def get(id_):
    """
    get company/ies
    """
    return firebase.get(CHILD, id_)

def update(id_, value):
    """
    update company
    """
    return firebase.update(CHILD, id_, value)