# Projektin_tyoaikaseuranta

https://projektintyoaikaseurantademo.herokuapp.com/

Sovellus on tarkoitettu henkilökohtaisten projektien aikataulujen seuraamiseen. Projekti voi tarkoittaa tässä yhteydessä mitä tahansa töistä tai opiskeluista harrastuksiin ja henkilökohtaisiin tavoitteisiin. Voidakseen käyttää sivustoa, käyttäjän tulee ensin tehdä käyttäjä ja kirjautua sivulle. Sisään kirjautumisen jälkeen käyttäjä voi aloittaa projektin antamalla sille nimen, minkä jälkeen projekti ilmestyy sivuston projektilistaan. Projektilistan kautta voit muokata projektia, esimerkiksi merkitä projektin valmistuneeksi. Jokainen projekti on käyttäjän henkilökohtainen, eli jokaisella käyttäjällä on pääsy vain omiin projekteihinsa.

Projektien työajan seuranta tapahtuu projektiin liittyvien työtehtävien avulla. Ajatuksena on, että jokainen projekti voidaan jakaa useisiin pieniin työtehtäviin, joilla jokaisella on nimi, työhön käytetty aika sekä tarkempi kuvaus tehdystä työstä. Työtehtävän kuvaukseen voi tehdä myös merkintöjä projektin etenemisestä. Jokaiseen projektiin liittyvät työtehtävät ja niiden tiedot on mahdollista saada näkyviin projektikohtaisesti.

Sivuston hyödyntämiseen on oikeastaan kaksi tapaa. Ensimmäinen on, että järjestelmään merkitään projektiin liittyvät työtehtävät sitä mukaa, kun projekti etenee, ja projektin valmistumisen jälkeen käyttäjä saa näkyviin projektin eteen tehdyt työt ja voi arvioida sitten näiden tietojen pohjalta, kuinka hyvin projektissa pysyttiin aikataulussa, mikä oli helppoa ja sujui nopeasti ja mikä toisaalta tuotti ongelmia ja mihin kului paljon aikaa. Näitä tietoja voi sitten hyödyntää seuraavaa projektia suunnitellessa.

Toinen tapa sovelluksen käyttämiseen on se, että käyttäjä käyttääkin sovellusta projektin suunnitteluvaiheessa apuna niin, että tekee ennakkoon aikataulun projektin toteutukselle. Tämä tarkoittaa sitä, että projektiin merkitään ennakkoon työtehtäviä, ja työtehtävälistaa käytetään sitten aikatauluna ja muistilistana, josta poistetaan tehdyt tehtävät sitä mukaa, kun ne valmistuvat. Projekti on valmis, kun kaikki sen osat on toteutettu ja projektin tehtävälista on tyhjä.



Sovelluksen tietokantakaavion saa näkyviin kopioimalla linkin alapuolella olevan tekstin tekstikenttään osoitteessa
https://yuml.me/diagram/scruffy/class/draw
%2F%2F Cool Class Diagram, [Projekti|(pk)id:Integer;(fk)käyttäjä_id:Käyttäjä;nimi:String;valmis:Boolean]monta-1[Käyttäjä|(pk)id:Integer;nimi:String;nimimerkki:String;salasana:String], [Työtehtävä|(pk)id:Integer;(fk)käyttäjä_id:Käyttäjä;(fk)projekti_id:Projekti;tehtävä:String;kuvaus:String;työtunnit:Integer]monta-1[Projekti], [Työtehtävä]monta-1[Käyttäjä]



Sovelluksen ominaisuudet ja toiminnallisuudet listattuna:

Sovellukseen voi tehdä uusia käyttäjiä.

Käyttäjän tulee kirjautua sisään voidakseen käyttää sovellusta.

Jokaisella käyttäjällä on pääsy vain omiin projekteihinsa.

Sovelluksessa voi lisätä uusia projekteja.

Projekteja voi merkitä valmiiksi tai keskeneräisiksi.

Projekteihin voi lisätä työtehtäviä ja kaikkia työtehtävän tietoja voi muokata jälkikäteen.

Työtehtäviä voi poistaa.

Kaikki yhteen projektiin liittyvät työtehtävät ja niihin liittyvät tiedot saa näkyviin projektikohtaisesti.

Projekteja voi poistaa, projektin poiston yhteydessä poistetaan myös kaikki siihen liittyvät työtehtävät.