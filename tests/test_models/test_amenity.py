#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""
    def setUp(self):
        """sets variable everytime"""
        Amenity.name = ""

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(Amenity())), res)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)
