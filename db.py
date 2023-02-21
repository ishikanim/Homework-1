""" database access
docs:
* http://initd.org/psycopg/docs/
* http://initd.org/psycopg/docs/pool.html
* http://initd.org/psycopg/docs/extras.html#dictionary-like-cursor
"""

from contextlib import contextmanager
import logging
import os
import json
from flask import current_app

import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import DictCursor

pool = None

def setup():
    global pool
    DATABASE_URL = os.environ['DATABASE_URL']
    pool = ThreadedConnectionPool(1, 100, dsn=DATABASE_URL, sslmode='require')


@contextmanager
def get_db_connection():
    try:
        connection = pool.getconn()
        yield connection
    finally:
        pool.putconn(connection)


@contextmanager
def get_db_cursor(commit=False):
    with get_db_connection() as connection:
      cursor = connection.cursor(cursor_factory=DictCursor)
      # cursor = connection.cursor()
      try:
          yield cursor
          if commit:
              connection.commit()
      finally:
          cursor.close()

def add_result(name,email,age,select,recommend,time):
    with get_db_cursor(True) as cur:
        cur.logger.info("Adding response")
        cur.execute("INSERT INTO data (nam, email, num, campusFrequency, recommend, timestampy) values (%s, %s, %s, %s, %s, %s)", (name, email, age, select, recommend, time))

def get_final_results():
    with get_db_cursor(True) as cur:
        cur.execute("select (row_to_json(t)::jsonb) FROM (SELECT * FROM data) t")
        return cur.fetchall()

if __name__ == "__main__":
    setup()