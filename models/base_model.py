#!/usr/bin/python3
'''contains class BaseModel'''
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()


class BaseModel():
    '''class that defines all common attributes/methods for other classes'''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        '''instantiation of class BaseModel
        args:
            *args(any): arguments
            **kwargs(dict): dictionary of key/pair attributes
        Return: Nothing'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"] and \
                       isinstance(value, str):
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)

    def __str__(self):
        '''return string representation
        Return: string representation'''
        self.__dict__.pop("_sa_instance_state", None)
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime
        Return: Current datetime'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__
        of the instance
        Return: dictionary'''
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] =  str(self.__class__.__name__)
        new_dict.pop("_sa_instance_state", None)
        return new_dict
        
    def delete(self):
        '''Method that deletes the current instance from the storage
        (models.storage) by calling the method delete
        Return: Nothing'''
        models.storage.delete(self)
