#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class test_place(unittest.TestCase):
    """Tests instances and methods from amenity class"""
    def setUp(self):
        """sets variable everytime"""
        Place.name = ""
        Place.city_id = ""
        Place.user_id = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(Place())), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertEqual(issubclass(Place, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(Place, 'city_id'), True)
        self.assertEqual(hasattr(Place, 'user_id'), True)
        self.assertEqual(hasattr(Place, 'name'), True)
        self.assertEqual(hasattr(Place, 'description'), True)
        self.assertEqual(hasattr(Place, 'number_rooms'), True)
        self.assertEqual(hasattr(Place, 'number_bathrooms'), True)
        self.assertEqual(hasattr(Place, 'max_guest'), True)
        self.assertEqual(hasattr(Place, 'price_by_night'), True)
        self.assertEqual(hasattr(Place, 'latitude'), True)
        self.assertEqual(hasattr(Place, 'logitude'), True)
        self.assertEqual(hasattr(Place, 'amenity_ids'), True)
