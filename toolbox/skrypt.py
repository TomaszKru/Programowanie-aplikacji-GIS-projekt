from errno import EROFS
from msilib.schema import Error
import sqlite3 as sl
import os
import arcpy

wybrana_sciezka = arcpy.GetParameterInfo()[4].value

wybrana_nazwa = str(arcpy.GetParameterInfo()[5].value) + ".dbf"

arcpy.env.workspace = os.path.abspath(os.getcwd())

sciezka = os.path.dirname(os.path.abspath(__file__))
sciezka = str(sciezka)
sciezka = sciezka.replace("\\", "/")

wybrane_dane = arcpy.GetParameterInfo()[0].value
wybrany_rok = str(arcpy.GetParameterInfo()[1].value)
wybrany_miesiac = str(arcpy.GetParameterInfo()[2].value)
wybrany_dzien = str(arcpy.GetParameterInfo()[3].value)

conds = []


if wybrany_rok != "None":
    wybrany_rok = "rok = " + wybrany_rok
    conds.append(wybrany_rok)


if wybrany_miesiac != "None":
    wybrany_miesiac = "miesiac = " + wybrany_miesiac
    conds.append(wybrany_miesiac)


if wybrany_dzien != "None":
    wybrany_dzien = "dzien = "   + wybrany_dzien
    conds.append(wybrany_dzien)

if conds:
    conds =" WHERE " + " and ".join(conds)
else:
    conds = ""


if wybrane_dane == "Meteorologiczne opady":
    table = arcpy.management.CreateTable(wybrana_sciezka, wybrana_nazwa, sciezka+"/template_opad.dbf")
    cur = arcpy.da.InsertCursor(str(wybrana_sciezka)+"/"+wybrana_nazwa, ['ID', 'KOD', 'STACJA', 'ROK', 'MIESIAC', 'DZIEN', 'SUMA_OPAD', 'RODZ_OPAD', 'WYS_SNIEG'])
    con = sl.connect(sciezka+"/opad.db")
    for row in con.execute('SELECT * FROM OPAD' + conds):
        id = row[0]
        kod = row[1]
        stacja = row[2]
        rok = row[3]
        miesiac = row[4]
        dzien = row[5]
        suma = row[6]
        rodzaj = row[7]
        wysokosc = row[8]
        wers = (int(id), int(kod), stacja, int(rok), int(miesiac), int(dzien), float(suma), str(rodzaj), int(wysokosc))
        cur.insertRow(wers)

if wybrane_dane == "Meteorologiczne klimat":
    table = arcpy.management.CreateTable(wybrana_sciezka, wybrana_nazwa, sciezka+"/template_klimat.dbf")

    cur = arcpy.da.InsertCursor(str(wybrana_sciezka)+"/"+wybrana_nazwa, ['ID', 'KOD', 'STACJA', 'ROK', 'MIESIAC', 'DZIEN', 'SR_TEMP', 'SR_WILG', 'SR_P_WIAT', 'SR_ZACHMU'])
    con = sl.connect(sciezka+'/klimat.db')
    for row in con.execute('SELECT * FROM KLIMAT' + conds):
        id = row[0]
        kod = row[1]
        stacja = row[2]
        rok = row[3]
        miesiac = row[4]
        dzien = row[5]
        temp = row[6]
        wilg = row[7]
        predk = row[8]
        zachmu = row[9]
        wers = (int(id), int(kod), stacja, int(rok), int(miesiac), int(dzien), float(temp), float(wilg), float(predk), float(zachmu))
        cur.insertRow(wers)

if wybrane_dane == "Hydrologiczne":
    table = arcpy.management.CreateTable(wybrana_sciezka, wybrana_nazwa, sciezka+"/template_hydro.dbf")

    cur = arcpy.da.InsertCursor(str(wybrana_sciezka)+"/"+wybrana_nazwa, ['ID', 'KOD', 'STACJA', 'RZEKA', 'ROK', 'MIE_HYDRO', 'DZIEN', 'STAN_WODY', 'PRZEPLYW', 'TEMP_WODY', 'MIESIAC'])

    con = sl.connect(sciezka+'/hydro.db')

    for row in con.execute('SELECT * FROM HYDRO' + conds):
        id = row[0]
        kod = row[1]
        stacja = row[2]
        rzeka = row[3]
        try:
            indeks = rzeka.index("(")
            rzeka = rzeka[0:indeks-1]
        except:
            pass
        rok = row[4]
        mie_hydro = row[5]
        dzien = row[6]
        stan = row[7]
        if stan == None:
            stan = -999
        przep = row[8]
        if przep == None:
            przep = -999.0
        temp = row[9]
        if temp == None:
            temp = -999.0
        miesiac = row[10]
        wers = (int(id), int(kod), stacja, rzeka, int(rok), int(mie_hydro), int(dzien), stan, przep, temp, int(miesiac))
        cur.insertRow(wers)


arcpy.SetParameter(6, table)

