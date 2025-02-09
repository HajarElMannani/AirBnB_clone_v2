#!/usr/bin/python3
'''class Review'''
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    '''class that inherits from BaseModel
    Attributes:
        place_id(str): the Place.id
        user_id(str): the User.id
        text(str): empty string'''
        
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id", ondelete='cascade'), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id", ondelete='cascade'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
