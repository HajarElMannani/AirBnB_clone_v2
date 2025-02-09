#!/usr/bin/python3
'''contains class User'''
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    '''class that inherits fron BaseModel'''
    __tablename__ = "users"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade="delete-orphan, all")
        reviews = relationship('Review', backref='user', cascade="delete-orphan, all")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
