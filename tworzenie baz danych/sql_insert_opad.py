import sqlite3 as sl

con = sl.connect('opad.db')

sql = """INSERT INTO OPAD (id, kod, stacja, rok, miesiac, dzien, suma_opad, rodzaj_opad, wys_sw_snieg) values(?, ?, ?, ?, ?, ?, ?, ?, ?)"""
data = []
rok = 2012
miesiac = 1
i = 0
while rok <= 2020:
    while miesiac <=12:
        miesiac_s = "{:02}".format(miesiac)
        wejscie = open(f"o_d_{miesiac_s}_{rok}.csv", "r")
        linia = wejscie.readline()
        while linia != "":
            krotka = ()
            linia = linia.split(",")
            linia0 = int(linia[0][1:-1])
            linia1 = linia[1][1:-1]
            linia2 = int(linia[2][1:-1])
            if linia[3][1:-2] == '0':
                linia3 = int(linia[3][2:-1])
            else:
                linia3 = int(linia[3][1:-1])
            if linia[4][1:-2] == '0':
                linia4 = int(linia[4][2:-1])
            else:
                linia4 = int(linia[4][1:-1])
            linia5 = float(linia[5])
            linia6 = linia[7]
            linia7 = float(linia[8])
            krotka = (i, linia0, linia1, linia2, linia3, linia4, linia5, linia6, linia7)
            data.append(krotka)
            i = i + 1
            linia = wejscie.readline()
        print(i)
        wejscie.close()
        miesiac = miesiac + 1
    rok = rok + 1
    miesiac = 1

con.executemany(sql, data)
con.commit()
print("Done")

