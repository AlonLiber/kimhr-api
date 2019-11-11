#!/usr/bin/env python

from firebase_admin import db


def get(child, id_):
    """
    firebase wrapper for get method
    """
    snapshot = db.reference().child(child).get()

    for key in snapshot:
        snapshot[key].update({"id": key})

    if id_:
        return [snapshot[key] for key in snapshot if id_ == key][0]

    return [snapshot[key] for key in snapshot]

def push(child, value):
    """
    firebase wrapper for push method
    """
    ref = db.reference().child(child).push()
    ref.set(value)

    return {
        "id": ref.key
    }

def update(child, id_, value):
    """
    firebase wrapper for update method
    """
    db.reference().child("%s/%s" % (child, id_)).update(value)

    return {
        "success": True
    }