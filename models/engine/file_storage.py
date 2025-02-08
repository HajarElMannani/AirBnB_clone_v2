#!/usr/bin/python3
'''class FileStorage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    '''serializes instances to a JSON file and deserializes
    JSON file to instances
    Attributes:
        __file_Path(str): name of json saving file
        __objects(dict): a dictionary'''

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''method that returns the dictionary objects
        Return: objects'''
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: value for key, value in FileStorage.__objects.items()
                    if isinstance(value, cls)}

    def new(self, obj):
        '''sets in __objects the obj with key
        args:
            obj(any): an object
        Return: Nothing'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file
        Return: Nothing'''
        object_dict = {obj: FileStorage.__objects[obj].to_dict()
                       for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as my_file:
            json.dump(object_dict, my_file)

    def reload(self):
        '''deserializes the JSON file to __objects
        Return: Nothing'''
        try:
            with open(FileStorage.__file_path) as my_file:
                dict_obj = json.load(my_file)
                for obj in dict_obj.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
        except json.decoder.JSONDecodeError:
            return

    def delete(self, obj=None):
        '''delete obj from __objects if it’s inside - if obj is equal to
        None, the method should not do anything
        Attributes:
        obj (any): object to delete
        Returns: Nothing'''
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
        else:
            return

    def close(self):
        '''call reload() method for deserializing the JSON file to objects'''
        self.reload()
