#!/user/bin/python3
'''class Place'''
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    '''class that inherits from BaseModel
    Attributes:
        city_id(str): the City.id
        user_id(str): the User.id
        name(str):  empty string
        description(str): empty string
        number_rooms(int): 0
        number_bathrooms(int): 0
        max_guest(int): 0
        price_by_night(int): 0
        latitude(float): 0.0
        longitude(float): 0.0
        amenity_ids(list): empty list: it will be the list of Amenity.id'''
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade='delete')
    amenities = relationship("Amenity", backref="place_amenities"secondary=place_amenity, viewonly=False)
    
    place_amenity = Table("place_amenity", Base.metadata, Column('place_id', String(60), PrimaryKey=True, Foreign_key('places.id'), nullable=False), Column('amenity_id', String(60), Primarykey=True, Foreign_key('amenities.id'), nullable=False))

    if (getenv("HBNB_TYPE_STORAGE", None) != "db"):
        @property
        def reviews(self):
            rev_instances = [inst_review for inst_review in storage.all(Review).values() if inst_review.place_id == self.id]
            return rev_instances

    
