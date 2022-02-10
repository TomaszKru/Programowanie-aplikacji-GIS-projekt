import urllib.request as ur
import zipfile as zf
import os
rok = 1951
miesiac = 1
while rok < 2021:
    if miesiac > 12:
        rok+=1
        miesiac = 1
    rok_s = str(rok)
    miesiac_s = "{:02}".format(miesiac)

    ur.urlretrieve("https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/"+rok_s+"/codz_"+rok_s+"_"+miesiac_s+".zip", "codz_"+rok_s+"_"+miesiac_s+".zip")
    print("downloaded")

    with zf.ZipFile("codz_"+rok_s+"_"+miesiac_s+".zip", "r") as zipped:
        zipped.extractall()
    os.remove("codz_"+rok_s+"_"+miesiac_s+".zip")
    print("Unzipped")
    miesiac+=1