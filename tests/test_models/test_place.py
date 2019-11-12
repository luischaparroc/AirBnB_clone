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

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(Place())), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertEqual(issubclass(Place, BaseModel), True)
