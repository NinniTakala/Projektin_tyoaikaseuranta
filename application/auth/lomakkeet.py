from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField
from wtforms import BooleanField, StringField, validators
  
class KirjautumisLomake(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class UusiKayttajaLomake(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    username = StringField("Käyttäjänimi", [validators.Length(min=2, max=144)])
    password = StringField("Salasana", [validators.Length(min=2, max=144)])
  
    class Meta:
        csrf = False
     
class LisaaTehtavia(FlaskForm):
    tehtava = StringField("Tehty työ", [validators.Length(min=2, max=150)])
    kuvaus = StringField("Työn kuvaus", [validators.Length(min=2, max=500)])
    tunnit = IntegerField("Käytetyt työtunnit", [validators.DataRequired()])
    
  
    class Meta:
        csrf = False