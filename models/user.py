#!/usr/bin/python3
'''contains class User'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''class that inherits fron BaseModel'''
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", back_populates="user", cascade="delete")
    reviews = relationship("Review", back_populates="user", cascade="delete")
