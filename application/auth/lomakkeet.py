from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import BooleanField, StringField, validators
  
class KirjautumisLomake(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class UusiKayttajaLomake(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    username = StringField("Käyttäjänimi", [validators.Length(min=2)])
    password = StringField("Salasana", [validators.Length(min=2)])
  
    class Meta:
        csrf = False