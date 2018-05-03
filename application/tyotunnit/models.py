from application import db
from application.models import Base

class Tyotunnit(Base):

    __tablename__ = "tyotunnit"

    tunnit = db.Column(db.Integer, nullable=False)
	
    projekti_id = db.Column(db.Integer, db.ForeignKey('projekti.id'),
                           nullable=False)
    
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                           nullable=False)
                         
    tyotehtava_id = db.Column(db.Integer, db.ForeignKey('tyotehtava.id'),
                           nullable=False)

    def __init__(self, tunnit):
        self.tunnit = tunnit
