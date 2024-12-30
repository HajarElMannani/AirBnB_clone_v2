#!/user/bin/python3
'''unittest for City class'''
import unittest
import os
from models.city import City
from models import storage
from datetime import datetime


class TestCity(unittest.TestCase):
    '''test class instantiation'''

    def test_init_no_arg(self):
        self.assertEqual(type(City()), City)

    def test_type_id(self):
        self.assertEqual(type(City().id), str)

    def test_id_unique(self):
        id1 = City().id
        id2 = City().id
        self.assertNotEqual(id1, id2)

    def test_state_id_str(self):
        self.assertEqual(type(City().state_id), str)

    def test_name_str(self):
        self.assertEqual(type(City().name), str)

    def test_created_at_type(self):
        self.assertEqual(type(City().created_at), datetime)

    def test_updated_at(self):
        self.assertEqual(type(City().updated_at), datetime)

    def test_instance_is_stored(self):
        self.assertIn(City(), storage.all().values())

    def test___str__(self):
        date = datetime.now()
        date_repr = repr(date)
        inst = City()
        inst.id = "j5454-547-kd54"
        inst.created_at = inst.updated_at = date
        bmstr = inst.__str__()
        self.assertIn("[City] (j5454-547-kd54)", bmstr)
        self.assertIn("'id': 'j5454-547-kd54'", bmstr)
        self.assertIn("'created_at': " + date_repr, bmstr)
        self.assertIn("'updated_at': " + date_repr, bmstr)

    def test_kwargs_inst(self):
        date = datetime.now()
        date_iso = date.isoformat()
        inst = City(id="35445", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(inst.id, "35445")
        self.assertEqual(inst.created_at, date)
        self.assertEqual(inst.updated_at, date)

    def test_args_and_kwargs_inst(self):
        date = datetime.now()
        date_iso = date.isoformat()
        inst = City("3", id="32145", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(inst.id, "32145")
        self.assertEqual(inst.created_at, date)
        self.assertEqual(inst.updated_at, date)


class TestSave(unittest.TestCase):
    '''Test Save'''

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

    def test_save(self):
        inst = City()
        updated_at = inst.updated_at
        inst.save()
        self.assertLess(updated_at, inst.updated_at)

    def test_save_arg(self):
        inst = City()
        with self.assertRaises(TypeError):
            inst.save(None)

    def test_save_updated(self):
        inst = City()
        inst.save()
        bmid = "City." + inst.id
        with open("file.json", "r") as my_file:
            self.assertIn(bmid, my_file.read())

    '''Test to_dict'''
    def test_to_dict_type(self):
        inst = City()
        self.assertTrue(type(inst.to_dict()), dict)

    def test_to_dict_keys(self):
        inst = City()
        self.assertIn("id", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())

    def test_to_dict_attributes(self):
        inst = City()
        inst.first_name = "Lilou"
        inst.address = 98
        self.assertIn("first_name", inst.to_dict())
        self.assertIn("address", inst.to_dict())

    def test_to_dict_output(self):
        date = datetime.now()
        inst = City()
        inst.id = "123l-o456-54sd"
        inst.created_at = inst.updated_at = date
        dict_content = {
            'id': '123l-o456-54sd',
            '__class__': 'City',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(inst.to_dict(), dict_content)

    def test_to_dict_datetime_attr_str(self):
        inst = City()
        inst_dict = inst.to_dict()
        self.assertEqual(str, type(inst_dict["created_at"]))
        self.assertEqual(str, type(inst_dict["updated_at"]))

    def test_to_dict_arg(self):
        inst = City()
        with self.assertRaises(TypeError):
            inst.to_dict(None)

    def test_deiff_to_dict_vs__dict(self):
        inst = City()
        self.assertNotEqual(inst.to_dict(), inst.__dict__)


if __name__ == "__main__":
    unittest.main()
