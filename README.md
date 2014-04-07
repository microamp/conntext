Conntext
========

Context managers for secure and atomic database connectivity

Goals
-----
* Each context being a single atomic process ("either all occur, or nothing occurs")
* No manual ``commit`` (success), ``rollback`` (fail) or ``close`` (either)
* No ORM

Usage
-----
```python
from conntext.conntext import conn, cursor
import sqlite3 as sqlite

with conn(sqlite.connect(":memory:", factory=sqlite.Row)) as conn_:
    with cursor(conn_.cursor()) as cursor_:
        cursor_.execute("CREATE TABLE person (name)")
```

License
-------

All the code is licensed under the GNU Lesser General Public License (v3+).