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
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="State", cascade="delete")

    if (getenv("HBNB_TYPE_STORAGE") != 'db'):
        @property
        def cities(self):
            '''Getter attribute that returns the list of City instances with state_id equals to the current State.id'''
            instaces = [city_inst for city_inst in storage.all(City).values() if (city_inst.state_id == self.id)]
            return instances
