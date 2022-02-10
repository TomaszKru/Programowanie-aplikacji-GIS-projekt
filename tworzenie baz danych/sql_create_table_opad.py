import sqlite3 as sl

con = sl.connect('opad.db')

sql = ("""
        CREATE TABLE OPAD (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            kod INTEGER,
            stacja TEXT,
            rok INTEGER,
            miesiac INTEGER,
            dzien INTEGER,
            suma_opad DOUBLE,
            rodzaj_opad TEXT,
            wys_sw_snieg DOUBLE
        )
""")

con.execute(sql)

