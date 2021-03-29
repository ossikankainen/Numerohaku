## Tämä ohjelma hakee puhelinnumeroita 0100100-palvelusta sukunimen kahden ensimmäisen kirjaimen perusteella.

import os

def main():
    try:
        osoite = input("Anna alueen osoite: ")

        alku = -1 # Alustetaan ei sallittuun arvoon while-looppia varten
        loppu = -1
        while (alku < 0 or alku > 383 or loppu < 0 or loppu > 383):
            print("Anna väli, jolta haluat hakea tulokset antamalla kaksi numeroa (1-383) erotettuna välilyönnillä.") 
            print("Painamalla enteriä ohjelma hakee kaikki tulokset.")
            vali = input("Anna väli: ")
            try:
                alku, loppu = vali.split()
                alku = int(alku)-1 # Numerointi alkaa nollasta, viimeistä ei palauteta eli viimeisenä saadaan 382
                loppu = int(loppu)
            except:
                alku = 0
                loppu = 383

        hakulausekkeet = muodostaHakulausekkeet(osoite,alku,loppu)
        haeNumero(hakulausekkeet)
    except:
        print("Ohjelman toiminnassa tapahtui virhe. Ota yhteyttä Ossiin ja kuvaile käyttötilanne, missä virhe tapahtui.")
        print("Ohjelman suoritus päättyi. Voit sulkea ikkunan ja mahdollisesti auenneen selaimen.")

def muodostaPolku(tiedosto):
    try:
        juuri = sys._MEIPASS # PyInstaller varten
    except Exception:
        juuri = os.path.abspath(".")

    return os.path.join(juuri,tiedosto)

def muodostaHakulausekkeet(osoite,alku,loppu):
    import csv

    polku = muodostaPolku("Sukunimet.csv")
    # Käydään läpi csv-tiedosto, joka sisältää listan sukunimien alkukirjaimista
    with open(polku) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        sukunimet = []
        for row in csv_reader:
            sukunimet.append(row[1])

    hakulausekkeet = [sukunimi + "*, " + osoite for sukunimi in sukunimet]
    hakulausekkeet = hakulausekkeet[alku:loppu] # Valitaan vain ne, jotka käyttäjä haluaa
    
    return hakulausekkeet

def tulostaTulokset(sisalto,kahva,tiedot,aakkoset,hakulauseke,eka_kerta):
    for i in range(len(sisalto)):
        if sisalto[0].text[0] == "L" and i != 0: # Onnistunut tulos alkaa sanalla 'Löytyi'. Ei tulosteta löytyneiden lukumäärää (i=0)
            if (hakulauseke.split("*")[0] not in aakkoset):
                aakkoset.append(hakulauseke.split("*")[0]) # Tallennetaan alkukirjaimet, joilla löytyi tuloksia
            
            if (kahva == "aakkoset"):
                if (eka_kerta == True):
                    print("Huom! Aakkoslistaus ei sisällä duplikaattitulosten poistoa.")
                    eka_kerta = False
                print(hakulauseke.split("*")[0])
                return tiedot,aakkoset,eka_kerta

            teksti = str(sisalto[i].text)
            teksti = teksti.split()
            nimi = teksti[1]
            
            if (kahva == "kaikki"):
                if nimi not in tiedot:
                    tiedot[nimi] = sisalto[i].text
                    print(sisalto[i].text)
            
            if (kahva == "tiivis"):
                if nimi not in tiedot:
                    numero = teksti[2]
                    operaattorit = {"040", "041", "042", "044", "045", "046", "050", "0400"}
                    indeksit = [i for i, v in enumerate(teksti) if v in operaattorit]
                    if (len(indeksit) > 0):
                        indeksi = indeksit[0]
                        numero = teksti[indeksi] + teksti[indeksi+1] + teksti[indeksi+2]
                    tiedot[nimi] = numero
                    print(nimi, numero)

    return tiedot,aakkoset,eka_kerta

def haeNumero(hakulausekkeet):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    # Tietorakenne auttaa duplikaattien käsittelyssä. Aakkosten kohdalla duplikaatteja ei käsitellä.
    tiedot = {}
    aakkoset = []
    eka_kerta = True

    print("Anna selain (Firefox/Chrome), jota haluat käyttää. Oletus on Chrome.")
    selain = input("Anna selain: ").lower()
    if (selain == "firefox"):
        geckodriver_polku = muodostaPolku('geckodriver.exe')
        driver = webdriver.Firefox(executable_path=geckodriver_polku)
        driver.get("https://hae.0100100.fi")
    else:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        chromedriver_polku = muodostaPolku("chromedriver.exe")
        driver = webdriver.Chrome(executable_path=chromedriver_polku,chrome_options = opts)   

    komento = ""
    while (komento == ""):
        print("Kirjaudu sisään syöttämällä auenneessa selaimessa käyttäjätunnuksesi ja salasanasi.")
        print("Kirjoita 'jatka' jatkaaksesi tai 'lopeta' sammuttaaksesi ohjelman.")
        syote = input("Anna syöte: ").lower()
        if (syote == "jatka" or syote == "lopeta"):
            komento = syote

    if (komento == "jatka"): # Tarkistetaan onko käyttäjä painanut enteriä
        sisalto = []

        print("Valitse tulostettavat tiedot (kaikki, tiivis, aakkoset). Oletus on kaikki.")
        print("Vaihtoehto kaikki tulostaa kaikki 0100100 löytyvät tiedot.")
        print("Vaihtoehto tiivis tulostaa nimen ja puhelinnumeron.")
        print("Vaihtoehto aakkoset tulostaa kirjaimet, joilla saatiin tuloksia.")
        kahva = input("Anna syöte: ").lower()
        if (kahva != "kaikki" and kahva != "tiivis" and kahva != "aakkoset"):
            kahva = "kaikki"

        #Haetaan osoitteen perusteella numerot
        print("Huom! Tuloksissa saattaa esiintyä numeroita, jotka eivät oikeasti sijaitse alueellasi.")
        print("Tämä johtuu siitä, miten 0100100 tulkitsee osoitteita.")
        for hakulauseke in hakulausekkeet:
            searchInputElement = driver.find_element_by_name('search')
            searchInputElement.clear()
            searchInputElement.send_keys(hakulauseke)
            searchInputElement.send_keys(Keys.ENTER)

            time.sleep(3) # Odota tulosten latautumista

            edellinen_sisalto = sisalto
            sisalto = driver.find_elements_by_class_name('entry')

            if (sisalto == edellinen_sisalto):
                time.sleep(60) # 0100100 ei suostu tekemään hakuja rajattoman tiheään
                searchInputElement.send_keys(Keys.ENTER)
                time.sleep(3)
                sisalto = driver.find_elements_by_class_name('entry')

            tiedot,aakkoset,eka_kerta = tulostaTulokset(sisalto,kahva,tiedot,aakkoset,hakulauseke,eka_kerta)

        print("Valitse tallennetaanko aakkoset, joilla tuloksia löytyi. Tallennuspaikka on kansio, jossa ohjelma ajetaan.")
        valinta = input("Talletaanko tiedot (kyllä/ei): ").lower()
        if (valinta == "kyllä"):
            nimi = input("Anna haluamasi tiedostonimi: ")
            with open(nimi+".txt",'w') as f:
                for aakkonen in aakkoset:
                    f.write("%s\n" % aakkonen)
     
    driver.close()
    print("Ohjelman suoritus päättyi. Voit sulkea ikkunan.")
    os._exit(1)

if __name__ == "__main__":
    main()