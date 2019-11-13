#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class test_city(unittest.TestCase):
    """Tests instances and methods from city class"""
    def setUp(self):
        """sets variable everytime"""
        City.state_id = ""
        City.name = ""

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(City())), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertEqual(issubclass(City, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(City, 'state_id'), True)
        self.assertEqual(hasattr(City, 'name'), True)
