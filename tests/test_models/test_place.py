#!/user/bin/python3
'''unittest for Place class'''
import unittest
import os
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    '''test class instantiation'''

    def test_init_no_arg(self):
        self.assertEqual(type(Place()), Place)

    def test_type_id(self):
        self.assertEqual(type(Place().id), str)

    def test_id_unique(self):
        id1 = Place().id
        id2 = Place().id
        self.assertNotEqual(id1, id2)

    def test_city_id_str(self):
        self.assertEqual(type(Place().city_id), str)

    def test_user_id_str(self):
        self.assertEqual(type(Place().user_id), str)

    def test_name_str(self):
        self.assertEqual(type(Place().name), str)

    def test_description_str(self):
        self.assertEqual(type(Place().description), str)

    def test_number_rooms_int(self):
        self.assertEqual(type(Place().number_rooms), int)

    def test_number_bathrooms_int(self):
        self.assertEqual(type(Place().number_bathrooms), int)

    def test_max_guest_int(self):
        self.assertEqual(type(Place().max_guest), int)

    def test_price_by_night_int(self):
        self.assertEqual(type(Place().price_by_night), int)

    def test_latitude_float(self):
        self.assertEqual(type(Place().latitude), float)

    def test_longitude_float(self):
        self.assertEqual(type(Place().longitude), float)

    def test_amenity_ids_list(self):
        self.assertEqual(type(Place().amenity_ids), list)

    def test_created_at_type(self):
        self.assertEqual(type(Place().created_at), datetime)

    def test_updated_at(self):
        self.assertEqual(type(Place().updated_at), datetime)

    def test_instance_is_stored(self):
        self.assertIn(Place(), storage.all().values())

    def test___str__(self):
        date = datetime.now()
        date_repr = repr(date)
        inst = Place()
        inst.id = "j5454-547-kd54"
        inst.created_at = inst.updated_at = date
        bmstr = inst.__str__()
        self.assertIn("[Place] (j5454-547-kd54)", bmstr)
        self.assertIn("'id': 'j5454-547-kd54'", bmstr)
        self.assertIn("'created_at': " + date_repr, bmstr)
        self.assertIn("'updated_at': " + date_repr, bmstr)

    def test_kwargs_inst(self):
        date = datetime.now()
        date_iso = date.isoformat()
        inst = Place(id="35445", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(inst.id, "35445")
        self.assertEqual(inst.created_at, date)
        self.assertEqual(inst.updated_at, date)

    def test_args_and_kwargs_inst(self):
        date = datetime.now()
        date_iso = date.isoformat()
        inst = Place("3", id="32145", created_at=date_iso, updated_at=date_iso)
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
        inst = Place()
        updated_at = inst.updated_at
        inst.save()
        self.assertLess(updated_at, inst.updated_at)

    def test_save_arg(self):
        inst = Place()
        with self.assertRaises(TypeError):
            inst.save(None)

    def test_save_updated(self):
        inst = Place()
        inst.save()
        bmid = "Place." + inst.id
        with open("file.json", "r") as my_file:
            self.assertIn(bmid, my_file.read())

    '''Test to_dict'''
    def test_to_dict_type(self):
        inst = Place()
        self.assertTrue(type(inst.to_dict()), dict)

    def test_to_dict_keys(self):
        inst = Place()
        self.assertIn("id", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())

    def test_to_dict_attributes(self):
        inst = Place()
        inst.first_name = "Lilou"
        inst.address = 98
        self.assertIn("first_name", inst.to_dict())
        self.assertIn("address", inst.to_dict())

    def test_to_dict_output(self):
        date = datetime.now()
        inst = Place()
        inst.id = "123l-o456-54sd"
        inst.created_at = inst.updated_at = date
        dict_content = {
            'id': '123l-o456-54sd',
            '__class__': 'Place',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(inst.to_dict(), dict_content)

    def test_to_dict_datetime_attr_str(self):
        inst = Place()
        inst_dict = inst.to_dict()
        self.assertEqual(str, type(inst_dict["created_at"]))
        self.assertEqual(str, type(inst_dict["updated_at"]))

    def test_to_dict_arg(self):
        inst = Place()
        with self.assertRaises(TypeError):
            inst.to_dict(None)

    def test_deiff_to_dict_vs__dict(self):
        inst = Place()
        self.assertNotEqual(inst.to_dict(), inst.__dict__)


if __name__ == "__main__":
    unittest.main()
