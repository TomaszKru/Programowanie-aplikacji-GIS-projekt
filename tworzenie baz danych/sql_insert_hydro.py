import sqlite3 as sl

con = sl.connect('test2.db')

sql = """INSERT INTO HYDRO (id, kod, stacja, rzeka, rok, miesiac_hydro, dzien, stan_wody, przeplyw, temp_wody, miesiac) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
data = []
rok = 2012
miesiac = 1
i = 0
while rok <= 2020:
    while miesiac <=12:
        miesiac_s = "{:02}".format(miesiac)
        wejscie = open(f"codz_{rok}_{miesiac_s}.csv", "r")
        linia = wejscie.readline()
        while linia != "":
            krotka = ()
            linia = linia.split(",")
            linia0 = int(linia[0][2:11])
            linia1 = linia[1][1:-1]
            linia2 = linia[2][1:-5]
            linia3 = int(linia[3][1:-1])
            if linia[4][1:-2] == '0':
                linia4 = int(linia[4][2:-1])
            else:
                linia4 = int(linia[4][1:-1])
            if linia[5][1:-2] == '0':
                linia5 = int(linia[5][2:-1])
            else:
                linia5 = int(linia[5][1:-1])
            if linia[6] == "9999":
                linia6 = None
            else:
                linia6 = int(linia[6])
            if linia[7] == "99999.999":
                linia7 = None
            else:
                linia7 = float(linia[7])
            if linia[8] == "99.9":
                linia8 = None
            else:
                linia8 = float(linia[8])
            if linia[9][1:-2] == '0':
                linia9 = int(linia[9][2:-2])
            else:
                linia9 = int(linia[9][1:-2])
            krotka = (i, linia0, linia1, linia2, linia3, linia4, linia5, linia6, linia7, linia8, linia9)
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

