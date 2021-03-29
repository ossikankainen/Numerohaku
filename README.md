# Numerohaku

Huom! GDPR-lainsäädäntö rajoittaa muistiinpanojen pitämistä. Ohjelmantekijä ei ota mitään vastuuta ohjelman väärinkäytöksistä.

Repositoriossa on toistaiseksi suoritettava ohjelmatiedosto ainoastaan Windowsille. Ohjelman koodi löytyy omasta kansiostaan ja sitä voi ajaa myös muilla käyttöjärjestelmillä, jos tietokoneelle on asennettu Python-tulkki. Ohjelman ensimmäisellä käyttökerralla käyttäjä joutuu todennäköisesti sallimaan sen toiminnan tietoturvaohjelmastaan. Tätä todennäköisesti ehdotetaan automaattisesti. Ohjelmasta otetaan mielellään vastaan palautetta.

Käyttöohjeet:
* Ensimmäisenä ohjelma kysyy alueen osoitetta. Syötä se samassa muodossa kuin syöttäisit sen 0100100-palveluun. (Esimerkkitie/Esimerkkitie 30/Esimerkkitie 30 12345 Toimipaikka)
* Ohjelman toiminta perustuu siihen, että se täydentää osoitteeseen automaattisesti sukunimen alkukirjaimia yleisyysjärjestyksessä. Seuraavana se kysyy, miltä väliltä sukunimilistasta tietoja halutaan hakea. Väli annetaan kahtena numerona väliltä 1-383, jotka on erotettu välilyönnillä. Jos väliä ei anneta, ohjelma hakee oletuksena tietoja koko listalla. Vinkki: Tämä mahdollistaa alueen tietojen hakemisen vähitellen. Voit aloittaa uuden haun siitä, mihin jäit viimeksi.
* Seuraavaksi ohjelma kysyy haluatko käyttää selaimena Firefoxia vai Chromea. Oletusvalinta on Chrome, mutta siinä on viime aikoina esiintynyt ongelmia.
* Ohjelma avaa automaattisesti uuden selainikkunan ja menee sivulle 0100100.fi. Kirjaudu sisään 0100100:aan selainikkunassa ja kirjoita sen jälkeen komento 'jatka' ohjelmaan. Komento 'lopeta' sammuttaa ohjelman. 
* Ohjelmassa voi valita 3 eri tavasta, miten tiedot näytetään. Oletus on kaikki.
  * Kaikki: Ohjelma näyttää kaikki tiedot, mitkä 0100100:kin. Toistuvat tulokset on poistettu.
  * Tiivis: Ohjelma näyttää etunimen ja puhelinnumeron. Nimi voi varsinkin yritysten kohdalla olla erikoisen näköinen. Jos puhelinnumeroa ei löydy, ohjelma näyttää etu- ja sukunimen. Toistuvat tulokset on poistettu. Huom! Osa tuloksista saattaa olla muilta alueilta, koska 0100100 hakee tietoja esimerkiksi asunnon numeron pohjalta. Älä siis luota täysin siihen, että kaikki numerot ovat alueeltasi.
  * Aakkoset: Ohjelma näyttää, millä alkukirjaimilla löytyi tuloksia. Toistuvia tuloksia ei ole poistettu.
* Ohjelma alkaa hakea itsenäisesti numeroita ja näyttää ne näytöllä. Välillä se pitää minuutin tauon. Se kuuluu tavalliseen ohjelman toimintaan.
* Viimeiseksi ohjelma kysyy haluaako käyttäjä tallentaa haetut tiedot. Tietojen laajuus on sama, mikä valittiin edellä. Päätös tapahtuu vastaamalla kyllä tai ei. Jos vastaus on kyllä, ohjelma kysyy tiedostonimeä. Tallennussijainti on sama kuin ohjelmatiedoston sijainti. Huom! Muista muistiinpanojen tekemistä koskevat rajoitukset.
