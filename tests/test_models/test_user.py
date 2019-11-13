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

    u = User()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertEqual(isinstance(self.u, BaseModel), True)
        self.assertEqual(isinstance(self.u, User), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        u = User()
        self.assertEqual(hasattr(self.u, 'email'), True)
        self.assertEqual(hasattr(self.u, 'password'), True)
        self.assertEqual(hasattr(self.u, 'first_name'), True)
        self.assertEqual(hasattr(self.u, 'last_name'), True)
        self.assertEqual(hasattr(self.u, 'id'), True)
        self.assertEqual(hasattr(self.u, 'created_at'), True)
        self.assertEqual(hasattr(self.u, 'updated_at'), True)

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertTrue(type(self.u.first_name), str)
        self.assertTrue(type(self.u.last_name), str)
        self.assertTrue(type(self.u.email), str)
        self.assertTrue(type(self.u.password), str)
        self.assertTrue(type(self.u.id), str)
        self.assertTrue(type(self.u.created_at), datetime.datetime)
        self.assertTrue(type(self.u.updated_at), datetime.datetime)

if __name__ == '__main__':
    unittest.main()
