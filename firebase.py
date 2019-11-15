#!/usr/bin/env python

from firebase_admin import db


class Firebase(object):

    def __init__(self, child):
        """
        constructor
        """
        self.child = child

    def get(self, id_):
        """
        firebase get
        """
        snapshot = db.reference().child(self.child).get()

        if not snapshot:
            return []

        for key in snapshot:
            snapshot[key].update({
                "id": key
            })

        if id_:
            return [snapshot[key] for key in snapshot if id_ == key]

        return [snapshot[key] for key in snapshot]

    def update(self, value):
        """
        firebase update
        """
        db.reference().child(self.child).update(value)

    def push(self, value):
        """
        firebase push
        """
        ref = db.reference().child(self.child).push()
        ref.set(value)

        return ref.key