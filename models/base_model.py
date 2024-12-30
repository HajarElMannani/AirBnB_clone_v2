#!/usr/bin/python3
'''contains class BaseModel'''
import uuid
from datetime import datetime
import models


class BaseModel():
    '''class that defines all common attributes/methods for other classes'''

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
        else:
            models.storage.new(self)

    def __str__(self):
        '''return string representation
        Return: string representation'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute updated_at with the
        current datetime
        Return: Current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__
        of the instance
        Return: dictionary'''
        return {
            **self.__dict__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__,
        }
