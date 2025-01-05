#!/usr/bin/python3
'''contains class City'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey 
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''class City
    Attributes:
        state_id(str): empty string: it will be the State.id
        name(str): empty string'''

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
