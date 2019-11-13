#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    p = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime.datetime)
        self.assertIsInstance(self.p.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
