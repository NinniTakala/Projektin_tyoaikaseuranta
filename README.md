# Projektin_tyoaikaseuranta

https://projektintyoaikaseurantademo.herokuapp.com/

Tavoitteena on tehdä järjestelmä, jolla voidaan seurata projekteihin käytettyä työaikaa. 
Järjestelmässä voidaan luoda uusia projekteja ja liittää työntekijöitä niihin. 
Jokainen työntekijä merkitsee tietokantaan työaikansa, tekemänsä tehtävälajin sekä mahdolliset lisätiedot tehdystä työstä. 
Projektipäällikkö voi nähdä yhteenvedon tehdyistä töistä joko viikoittain, henkilöittäin tai tehtävälajeittain. 
Työntekijät saavat halutessaan näkyviin omat työmerkintänsä.

Alustavan version lopullisen sovelluksen tietokantakaaviosta saa näkyviin kopioimalla linkin alla olevan tekstin tekstikenttään osoitteessa
https://yuml.me/diagram/scruffy/class/draw
%2F%2F Cool Class Diagram, [Työntekijä|(pk)id:Integer;etunimi:String; sukunimi:String],
[Projekti|(pk)id:Integer;(fk)projektipäällikkö_id:Projektipäällikkö;nimi:String;tavoite:String;kesken:Boolean;alkamisaika:Date;määräaika:Date],
[Projekti]*-1[Projektipäällikkö|(pk)id:Integer;etunimi:String; sukunimi:String], 
[Projekti]1-*[Työ|(pk)id:Integer;(fk)työntekijä_id:Työntekijä;(fk)projekti_id:Projekti;työviikkko:Integer;työtunnit:double;työtehtävä:String;lisätiedot:String],
[Työ]*-1[Työntekijä]

