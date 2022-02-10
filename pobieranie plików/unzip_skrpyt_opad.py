import urllib.request as ur
import zipfile as zf
import os
rok = 2012
miesiac = 1
while rok < 2021:
    if miesiac > 12:
        rok+=1
        miesiac = 1
    rok_s = str(rok)
    miesiac_s = "{:02}".format(miesiac)

    ur.urlretrieve("https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/opad/"+rok_s+"/"+rok_s+"_"+miesiac_s+"_o.zip", rok_s+"_"+miesiac_s+"_o.zip")
    print("downloaded")

    with zf.ZipFile(rok_s+"_"+miesiac_s+"_o.zip", "r") as zipped:
        zipped.extractall()
    os.remove(rok_s+"_"+miesiac_s+"_o.zip")
    print("Unzipped")
    miesiac+=1