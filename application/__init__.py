from flask import Flask
app = Flask(__name__)
  
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projektit.db"    
    app.config["SQLALCHEMY_ECHO"] = True

  
db = SQLAlchemy(app)
  
from application.projektit import models
from application.projektit import views
  
from application.auth import models
from application.auth import views

from application.tyotehtavat import models
from application.tyotehtavat import views

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "kirjautuminen"
login_manager.login_message = "Kirjaudu sivulle"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass









