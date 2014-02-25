conntext
========

Context managers for MySQL/SQLite connectivity

Requirements
------------
* MySQL-python>=1.2.5 (for MySQL)
* pysqlite>=2.b6.3 (for SQLite)


Usage
-----
```
from conntext.conntext import conn, cursor, DB_TYPE_SQLITE

with conn(DB_TYPE_SQLITE, "/tmp/conntexttest") as conn:
    with cursor(conn) as cursor:
        cursor.execute("INSERT ...")
```
