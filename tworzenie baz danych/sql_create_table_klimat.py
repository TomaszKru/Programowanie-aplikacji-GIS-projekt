import sqlite3 as sl

con = sl.connect('klimat.db')

sql = ("""
        CREATE TABLE KLIMAT (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            kod INTEGER,
            stacja TEXT,
            rok INTEGER,
            miesiac INTEGER,
            dzien INTEGER,
            sr_temp DOUBLE,
            sr_wilg DOUBLE,
            sr_p_wiatru DOUBLE,
            sr_zachmu DOUBLE
        )
""")

con.execute(sql)

