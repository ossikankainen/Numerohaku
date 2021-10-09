# Numerohaku

Huom! GDPR-lainsäädäntö rajoittaa muistiinpanojen pitämistä. Ohjelmantekijä ei ota mitään vastuuta ohjelman väärinkäytöksistä.

Repositoriossa on toistaiseksi suoritettava ohjelmatiedosto ainoastaan Windowsille. Ohjelman koodi löytyy omasta kansiostaan ja sitä voi ajaa myös muilla käyttöjärjestelmillä, jos tietokoneelle on asennettu Python-tulkki. Ohjelman ensimmäisellä käyttökerralla käyttäjä joutuu todennäköisesti sallimaan sen toiminnan tietoturvaohjelmastaan. Tätä todennäköisesti ehdotetaan automaattisesti. Ohjelmasta otetaan mielellään vastaan palautetta.

Käyttöohjeet:
* Ensimmäisenä ohjelma kysyy alueen osoitetta. Syötä se samassa muodossa kuin syöttäisit sen 0100100-palveluun. (Esimerkkitie/Esimerkkitie 30/Esimerkkitie 30 12345 Toimipaikka)
* Ohjelman toiminta perustuu siihen, että se täydentää osoitteeseen automaattisesti yleisimpiä sukunimen alkukirjaimia. Seuraavana se kysyy, miltä väliltä sukunimilistasta tietoja halutaan hakea. Väli annetaan kahtena numerona väliltä 1-253, jotka on erotettu välilyönnillä. Jos väliä ei anneta, ohjelma hakee oletuksena tietoja koko listalla. Vinkki: Tämä mahdollistaa alueen tietojen hakemisen vähitellen. Voit aloittaa uuden haun siitä, mihin jäit viimeksi.
* Seuraavaksi ohjelma kysyy haluatko käyttää selaimena Firefoxia vai Chromea. Oletus on Chrome. Ohjelman toiminta on testattu Firefoxin versiolla
93 ja Chromen versiolla 94.
* Ohjelma avaa automaattisesti uuden selainikkunan ja menee sivulle 0100100.fi.
* Ohjelma näyttää, millä alkukirjaimilla löytyi tuloksia. Toistuvia tuloksia ei ole poistettu. Huom! Edellisissä versiossa olleet muut esitystavat
on poistettu uusimmasta versiosta.
* Ohjelma alkaa hakea itsenäisesti numeroita ja näyttää ne näytöllä. Välillä se pitää puolen minuutin tauon. Se kuuluu tavalliseen ohjelman toimintaan ja johtuu 0100100:n rajoituksista.
* Viimeiseksi ohjelma kysyy haluaako käyttäjä tallentaa aakkoset, joilla saatiin tuloksia. Päätös tapahtuu vastaamalla kyllä tai ei. Jos vastaus on kyllä, ohjelma kysyy tiedostonimeä. Tallennussijainti on sama kuin ohjelmatiedoston sijainti. Huom! Muista muistiinpanojen tekemistä koskevat rajoitukset.