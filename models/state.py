#!/user/bin/python3
'''contains classes State'''
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    '''class state'''
    if (models.getenv("HBNB_TYPE_STORAGE") == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """instantiate state"""
        super().__init__(*args, **kwargs)

    if (models.getenv("HBNB_TYPE_STORAGE") != 'db'):
        @property
        def cities(self):
            '''Getter attribute that returns the list of City instances
            with state_id equals to the current State.id'''
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
