from application import db
from application.tyotehtavat.models import Tyotehtava
from application.models import Base

class Projekti(Base):

    name = db.Column(db.String(150), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
	
    account_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                           nullable=False)
						   
    tyotehtava = db.relationship("Tyotehtava", backref='projekti', lazy=True)

    def __init__(self, name):
        self.name = name
        self.done = False
		
		
  
