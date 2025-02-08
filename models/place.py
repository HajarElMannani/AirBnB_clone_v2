#!/user/bin/python3
'''class Place'''
import models
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv


if models.getenv('HBNB_TYPE_STORAGE') == 'db':
    table_a = Table("place_amenity", Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


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
    if models.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", backref="place_amenities", secondary='place_amenity', viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
        
    if models.getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            '''amenities setter '''
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
