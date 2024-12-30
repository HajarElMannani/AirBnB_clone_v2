#!/usr/bin/python3
'''contains class City'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class City
    Attributes:
        state_id(str): empty string: it will be the State.id
        name(str): empty string'''

    state_id = ""
    name = ""
