from sqlalchemy import Column, Integer, String

from dbconfig import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    age = Column(Integer)
    role = Column(String(255))