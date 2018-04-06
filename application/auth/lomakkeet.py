from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class KirjautumisLomake(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False