""" database access
docs:
* http://initd.org/psycopg/docs/
* http://initd.org/psycopg/docs/pool.html
* http://initd.org/psycopg/docs/extras.html#dictionary-like-cursor
"""

from contextlib import contextmanager
import logging
import os

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

def add_fact(source, content):
    with get_db_cursor(True) as cur:
        cur.execute("INSERT INTO facts (source, content) values (%s, %s)", (source, content))

def get_fact(id):
    with get_db_cursor(False) as cur:
        cur.execute("select * from facts where id = %s", (id,))
        return cur.fetchone()

def get_random_fact():
    with get_db_cursor(False) as cur:
        cur.execute("select * from facts order by random() limit 1;")
        return cur.fetchone()

def login(username, password):
    with get_db_cursor(False) as cur:
        cur.execute("select * from bad_way_to_do_users where username = '"+username+"' and password = '" + password+"';")
        return cur.fetchone()


if __name__ == "__main__":
    setup()
    print(login("kluver';--", "wrong"))
