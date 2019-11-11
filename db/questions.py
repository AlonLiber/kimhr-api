#!/usr/bin/env python

from db import firebase
from firebase_admin import db

# firebase child
CHILD = "questions"


def push(value):
    """
    add question
    """
    return firebase.push(CHILD, value)

def get(id_):
    """
    get question/s
    """
    return firebase.get(CHILD, id_)

def update(id_, value):
    """
    update question
    """
    return firebase.update(CHILD, id_, value)