from sqlalchemy import Column, Integer, String
from db.database import get_db

db = get_db()
class User(db.Model):
    __tablename__ = 'user'
    uid = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    gender = Column(Integer)

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender