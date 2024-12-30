#!/usr/bin/python3
'''contains class User'''
from models.base_model import BaseModel


class User(BaseModel):
    '''class that inherits fron BaseModel'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
