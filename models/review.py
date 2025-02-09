#!/usr/bin/python3
'''class Review'''
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer
from os import getenv


class Review(BaseModel, Base):
    '''class that inherits from BaseModel
    Attributes:
        place_id(str): the Place.id
        user_id(str): the User.id
        text(str): empty string'''
    __tablename__ = "reviews"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(Integer, primary_key=True)
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
