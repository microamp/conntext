#-*- coding: utf-8 -*-

from contextlib import contextmanager
from logging import getLogger

logger = getLogger(__name__)


@contextmanager
def conn(connect, *args, **kwargs):
    conn = connect(*args, **kwargs)
    try:
        yield conn
    except Exception as e:
        logger.error(e.message)
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
    except Exception as e:
        logger.error(e.message)
        raise
    finally:
        cursor.close()
