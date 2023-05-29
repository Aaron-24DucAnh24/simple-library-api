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
    record_id = 'bookid' if table=='books' else 'userid'
    cur = get_db().cursor()
    cur.execute(f'select max({record_id}) from {table};')
    _, ret = cur.fetchone().popitem()
    return ret + 1 if ret else 1
