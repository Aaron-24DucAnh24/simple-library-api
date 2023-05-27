import sqlite3
from flask import g
import os

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(os.environ.get('DATABASE'))
        db.row_factory = make_dicts
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def create_id(table):
    cur = get_db().cursor()
    cur.execute(f'select max(bookid) from {table};')
    _, ret = cur.fetchone().popitem()
    cur.close()
    return ret + 1
