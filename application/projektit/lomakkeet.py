from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ProjektiLomake(FlaskForm):
    name = StringField("Projektin nimi", [validators.Length(min=2)])
    done = BooleanField("Projekti käynnissä")
  
    class Meta:
        csrf = False