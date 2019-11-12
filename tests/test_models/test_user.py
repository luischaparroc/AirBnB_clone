#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    """Tests instances and methods from user class"""
    def setUp(self):
        """sets variable everytime"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(User())), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertEqual(issubclass(User, BaseModel), True)
