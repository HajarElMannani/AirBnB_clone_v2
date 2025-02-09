#!/usr/bin/python3
'''class Amenity'''
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
#from models import place

class Amenity(BaseModel, Base):
    '''class that inherits from BaseModel
    Attributes:
        name(str): empty string'''
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        #place_amenities = relationship("Place", secondary=place.place_amenity, viewonly=False)
    else:
        name = ''
