#-*- coding: utf-8 -*-

import os
import unittest
import sqlite3 as sqlite
import logging
from uuid import uuid4

from conntext.conntext import conn, cursor

logging.disable(logging.ERROR)


class TestConntext(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_db = "test-{0}.db".format(uuid4())
        with conn(sqlite.connect(cls.test_db)) as conn_:
            with cursor(conn_.cursor()) as cursor_:
                cursor_.execute("DROP TABLE IF EXISTS person")
                cursor_.execute("CREATE TABLE person (name)")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_db)

    def setUp(self):
        with conn(sqlite.connect(self.test_db)) as conn_:
            with cursor(conn_.cursor()) as cursor_:
                cursor_.execute("DELETE FROM person")

    def tearDown(self):
        pass

    def test_successful(self):
        with conn(sqlite.connect(self.test_db)) as conn_:
            with cursor(conn_.cursor()) as cursor_:
                cursor_.execute("SELECT name FROM person")
                self.assertEqual(cursor_.fetchall(), [])
                cursor_.execute("INSERT INTO person (name) "
                                "VALUES (?)", ["microamp"])

        with conn(sqlite.connect(self.test_db)) as conn_:
            with cursor(conn_.cursor()) as cursor_:
                cursor_.execute("SELECT name FROM person")
                self.assertEqual(cursor_.fetchall(), [("microamp",)])

    def test_failed(self):
        with self.assertRaises(sqlite.OperationalError):
            with conn(sqlite.connect(self.test_db)) as conn_:
                with cursor(conn_.cursor()) as cursor_:
                    cursor_.execute("SELECT name FROM person")
                    self.assertEqual(cursor_.fetchall(), [])
                    cursor_.execute("INSERT INTO person (name) "
                                    "VALUES (?)", ["microamp"])
                    cursor_.execute("INSERT INTO people (name) "
                                    "VALUES (?)", ["microamp"])

        with conn(sqlite.connect(self.test_db)) as conn_:
            with cursor(conn_.cursor()) as cursor_:
                cursor_.execute("SELECT name FROM person")
                self.assertEqual(cursor_.fetchall(), [])


if __name__ == "__main__":
    unittest.main()
