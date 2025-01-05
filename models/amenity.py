#!/usr/bin/python3
'''class Amenity'''
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''class that inherits from BaseModel
    Attributes:
        name(str): empty string'''

    __tablename__ == "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
