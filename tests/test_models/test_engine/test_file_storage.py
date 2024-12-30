#!/usr/bin/python3
'''Test the class FileStorage'''
import unittest
import os
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    '''Test the class FileStorage'''

    def test_FileStorage_inst(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_file_path__str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_type_storage(self):
        self.assertEqual(type(storage), FileStorage)

    def test_objects__dict(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test__instantiation_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    '''Test methods'''

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_type_all(self):
        self.assertEqual(type(storage.all()), dict)

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        base = BaseModel()
        storage.new(base)
        user = User()
        storage.new(user)
        state = State()
        storage.new(state)
        place = Place()
        storage.new(place)
        city = City()
        storage.new(city)
        amenity = Amenity()
        storage.new(amenity)
        review = Review()
        storage.new(review)
        self.assertIn("BaseModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn(user, storage.all().values())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn(state, storage.all().values())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn(place, storage.all().values())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn(city, storage.all().values())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())
        self.assertIn(amenity, storage.all().values())
        self.assertIn("Review." + review.id, storage.all().keys())
        self.assertIn(review, storage.all().values())

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_new_two_args(self):
        with self.assertRaises(TypeError):
            storage.new(User(), "l")

    '''Test save'''

    def test_save(self):
        text = ""
        base = BaseModel()
        storage.new(base)
        user = User()
        storage.new(user)
        state = State()
        storage.new(state)
        place = Place()
        storage.new(place)
        city = City()
        storage.new(city)
        amenity = Amenity()
        storage.new(amenity)
        review = Review()
        storage.new(review)
        storage.save()
        with open("file.json", "r") as my_file:
            text = my_file.read()
            self.assertIn("BaseModel." + base.id, text)
            self.assertIn("User." + user.id, text)
            self.assertIn("State." + state.id, text)
            self.assertIn("Place." + place.id, text)
            self.assertIn("City." + city.id, text)
            self.assertIn("Amenity." + amenity.id, text)
            self.assertIn("Review." + review.id, text)

    def test_save_args(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    '''Test reload'''
    def test_reload(self):
        base = BaseModel()
        storage.new(base)
        user = User()
        storage.new(user)
        state = State()
        storage.new(state)
        place = Place()
        storage.new(place)
        city = City()
        storage.new(city)
        amenity = Amenity()
        storage.new(amenity)
        review = Review()
        storage.new(review)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + base.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("User." + user.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("State." + state.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("Place." + place.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("City." + city.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("Amenity." + amenity.id,
                      FileStorage._FileStorage__objects)
        self.assertIn("Review." + review.id,
                      FileStorage._FileStorage__objects)

    def test_reload_args(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
