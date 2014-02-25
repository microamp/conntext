#-*- coding: utf-8 -*-

from contextlib import contextmanager
from functools import partial

import MySQLdb as mysql
import sqlite3 as sqlite

from .error import DatabaseNotSupported

DB_TYPE_MYSQL = 0
DB_TYPE_SQLITE = 1

connect = {DB_TYPE_MYSQL: partial(mysql.connect),
           DB_TYPE_SQLITE: partial(sqlite.connect)}


@contextmanager
def conn(type_, *args, **kwargs):
    if type_ not in connect.keys():
        raise DatabaseNotSupported("Type not supported: {0}".format(type_))

    conn = connect[type_](*args, **kwargs)

    try:
        yield conn
    except:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


@contextmanager
def cursor(conn):
    cursor = conn.cursor()

    try:
        yield cursor
    except:
        raise
    finally:
        cursor.close()
