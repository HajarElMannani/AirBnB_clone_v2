#!/usr/bin/python3
'''contains class User'''
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    '''class that inherits fron BaseModel'''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        id = Column(String(60), primary_key=True, nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade="delete")
        reviews = relationship('Review', backref='user', cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
