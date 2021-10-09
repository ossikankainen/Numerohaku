## Tämä ohjelma hakee puhelinnumeroita 0100100-palvelusta sukunimen neljän ensimmäisen kirjaimen perusteella

import sys
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    # try:
    NIMIEN_MAARA = 253

    osoite = input("Anna alueen osoite: ")

    alku = -1 # Alustetaan muuttujat ei sallittuun arvoon while-looppia varten
    loppu = -1

    while (alku < 0 or alku > NIMIEN_MAARA or loppu < 0 or loppu > NIMIEN_MAARA):
        print("Anna väli, jolta haluat hakea tulokset antamalla kaksi numeroa (1-{}) erotettuna välilyönnillä.".format(NIMIEN_MAARA)) 
        print("Painamalla enteriä ohjelma hakee kaikki tulokset.")
        vali = input("Anna väli: ")
        try:
            alku, loppu = vali.split()
            alku = int(alku)-1 # Numerointi alkaa nollasta, viimeistä ei palauteta eli viimeisestä ei kuulu vähentää yhtä
            loppu = int(loppu)
        except:
            alku = 0
            loppu = NIMIEN_MAARA

    hakulausekkeet = muodostaHakulausekkeet(osoite,alku,loppu)
    haeNumero(hakulausekkeet)
    # except:
    #     print("Ohjelman toiminnassa tapahtui virhe. Ota yhteyttä Ossiin ja kuvaile käyttötilanne, missä virhe tapahtui.")
    #     print("Ohjelman suoritus päättyi. Voit sulkea ikkunan ja mahdollisesti auenneen selaimen.")

def muodostaPolku(tiedosto):
    try:
        juuri = sys._MEIPASS # PyInstaller varten
    except Exception:
        juuri = os.path.abspath(".")

    return os.path.join(juuri,tiedosto)

def muodostaHakulausekkeet(osoite,alku,loppu):
    TIEDOSTONIMI = "sukunimet_uusi.csv"

    polku = muodostaPolku(TIEDOSTONIMI)
    # Käydään läpi csv-tiedosto, joka sisältää listan sukunimien alkukirjaimista
    with open(polku, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        sukunimet = []
        for row in csv_reader:
            sukunimi = row[0]
            sukunimet.append(sukunimi)

    hakulausekkeet = [sukunimi + "*, " + osoite for sukunimi in sukunimet]
    hakulausekkeet = hakulausekkeet[alku:loppu] # Valitaan vain ne, jotka käyttäjä haluaa
    
    return hakulausekkeet

def tulostaTulokset(sisalto, aakkoset, hakulauseke):
    for i in range(len(sisalto)):
        if sisalto[0].text[0] == "L" and i != 0: # Onnistunut tulos alkaa sanalla 'Löytyi'. Ei tulosteta löytyneiden lukumäärää (i=0)
            if (hakulauseke.split("*")[0] not in aakkoset):
                aakkoset.append(hakulauseke.split("*")[0]) # Tallennetaan alkukirjaimet, joilla löytyi tuloksia       
                print(hakulauseke.split("*")[0])
                return aakkoset

    return aakkoset

def haeNumero(hakulausekkeet):
    print("Anna selain (Firefox/Chrome), jota haluat käyttää. Oletus on Chrome.")
    selain = input("Anna selain: ").lower()
    if (selain == "firefox"):
        geckodriver_polku = muodostaPolku('geckodriver.exe')
        driver = webdriver.Firefox(executable_path=geckodriver_polku, service_log_path=os.devnull)
    else:
        opts = webdriver.ChromeOptions()
        opts.add_argument("--log-level=3")
        chromedriver_polku = muodostaPolku("chromedriver.exe")
        driver = webdriver.Chrome(executable_path=chromedriver_polku, chrome_options=opts)

    driver.get("https://hae.0100100.fi")

    print("Ohjelma tulostaa kirjainyhdistelmät, joilla löytyy tuloksia.")
    print("Huom! Tuloksissa saattaa esiintyä numeroita, jotka eivät oikeasti sijaitse alueellasi.")

    sisalto = []
    aakkoset = []

    #Haetaan osoitteen perusteella numerot
    for hakulauseke in hakulausekkeet:
        searchInputElement = driver.find_element_by_name('search')
        searchInputElement.clear()
        searchInputElement.send_keys(hakulauseke)
        searchInputElement.send_keys(Keys.ENTER)

        time.sleep(2) # Odota tulosten latautumista

        edellinen_sisalto = sisalto
        sisalto = driver.find_elements_by_class_name('entry')

        if (sisalto == edellinen_sisalto):
            time.sleep(30) # 0100100 ei suostu tekemään hakuja rajattoman tiheään
            searchInputElement.send_keys(Keys.ENTER)
            time.sleep(2)
            sisalto = driver.find_elements_by_class_name('entry')

        aakkoset = tulostaTulokset(sisalto, aakkoset, hakulauseke)

    driver.close()

    print("Valitse tallennetaanko aakkoset, joilla tuloksia löytyi. Tallennuspaikka on kansio, jossa ohjelma ajetaan.")
    valinta = input("Talletaanko tiedot (kyllä/ei): ").lower()
    if (valinta == "kyllä"):
        nimi = input("Anna haluamasi tiedostonimi: ")
        with open(nimi+".txt", 'w', encoding="utf-8") as f:
            for aakkonen in aakkoset:
                f.write("%s\n" % aakkonen)
     
    print("Ohjelman suoritus päättyi. Voit sulkea ikkunan.")
    os._exit(1)

if __name__ == "__main__":
    main()