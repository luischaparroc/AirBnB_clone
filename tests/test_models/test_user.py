#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import os
from models import storage
import datetime


class UserCase(unittest.TestCase):
    """Tests instances and methods from user class"""

    def test_class_exists(self):
        """tests if class exists"""
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        u = User()
        self.assertEqual(isinstance(u, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        u = User()
        self.assertEqual(hasattr(u, 'email'), True)
        self.assertEqual(hasattr(u, 'password'), True)
        self.assertEqual(hasattr(u, 'first_name'), True)
        self.assertEqual(hasattr(u, 'last_name'), True)
        self.assertEqual(hasattr(u, 'id'), True)
        self.assertEqual(hasattr(u, 'created_at'), True)
        self.assertEqual(hasattr(u, 'updated_at'), True)

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        usr = User()
        self.assertTrue(type(usr.first_name), str)
        self.assertTrue(type(usr.last_name), str)
        self.assertTrue(type(usr.email), str)
        self.assertTrue(type(usr.password), str)
        self.assertTrue(type(usr.id), str)
        self.assertTrue(type(usr.created_at), datetime.datetime)
        self.assertTrue(type(usr.updated_at), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
