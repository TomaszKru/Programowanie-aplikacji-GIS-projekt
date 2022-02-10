import sqlite3 as sl

con = sl.connect('test2.db')

sql = ("""
        CREATE TABLE HYDRO (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            kod INTEGER,
            stacja TEXT,
            rzeka TEXT,
            rok INTEGER,
            miesiac_hydro INTEGER,
            dzien INTEGER,
            stan_wody INTEGER,
            przeplyw DOUBLE,
            temp_wody DOUBLE,
            miesiac INTEGER
        )
""")

con.execute(sql)

