#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    """Tests instances and methods from amenity class"""
    def setUp(self):
        """sets variable everytime"""
        State.name = ""

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(State())), res)

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertEqual(issubclass(State, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(State, 'name'), True)
