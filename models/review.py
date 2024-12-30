#!/usr/bin/python3
'''class Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class that inherits from BaseModel
    Attributes:
        place_id(str): the Place.id
        user_id(str): the User.id
        text(str): empty string'''

    place_id = ""
    user_id = ""
    text = ""
