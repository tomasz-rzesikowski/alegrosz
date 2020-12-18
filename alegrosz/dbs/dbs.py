import os
import sqlite3

from flask import g

db_abs_path = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(db_abs_path, '..', 'alegrosz.db')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_path)

    return db
