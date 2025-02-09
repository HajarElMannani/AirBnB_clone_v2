#!/usr/bin/python3
'''contains class City'''
import models
import sqlalchemy
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''class City
    Attributes:
        state_id(str): empty string: it will be the State.id
        name(str): empty string'''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place', backref='cities', cascade="all")
    else:
        state_id = ""
        name = ""
