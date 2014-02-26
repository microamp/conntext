conntext
========

Context managers for database connectivity

Goals
-----
* Encourage use of SQL (no ORM)
* Each context is a single atomic process ("either all occur, or nothing occurs")
* No manual ``commit`` (success), ``rollback`` (fail) or ``close`` (always)

Usage
-----
```
from conntext.conntext import conn, cursor
import sqlite3 as sqlite

with conn(sqlite.connect, ":memory:", factory=sqlite.Row) as conn:
    with cursor(conn) as cursor:
        cursor.execute("your_sql_statement")
```