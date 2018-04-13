from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class UusiKayttajaLomake(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    username = StringField("Käyttäjänimi", [validators.Length(min=2)])
    password = StringField("Salasana", [validators.Length(min=2)])
  
    class Meta:
        csrf = False