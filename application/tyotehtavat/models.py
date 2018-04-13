from application import db
from application.models import Base

class Tyotehtava(Base):

    __tablename__ = "tyotehtava"

    tehtava = db.Column(db.String(150), nullable=False)
    kuvaus = db.Column(db.String(500), nullable=False)
	
    projekti_id = db.Column(db.Integer, db.ForeignKey('projekti.id'),
                           nullable=False)
	

    def __init__(self, tehtava):
        self.tehtava = tehtava
        self.kuvaus = kuvaus
