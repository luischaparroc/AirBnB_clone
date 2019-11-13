#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import os
from models import storage


class test_user(unittest.TestCase):
    """Tests instances and methods from user class"""

    def tearDown(self):
        """Method invoked for each test"""
        if os.path.exists(storage._FileStorage__file_path) is True:
            os.remove(storage._FileStorage__file_path)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(User())), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertEqual(issubclass(User, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(User, 'email'), True)
        self.assertEqual(hasattr(User, 'password'), True)
        self.assertEqual(hasattr(User, 'first_name'), True)
        self.assertEqual(hasattr(User, 'last_name'), True)

    def testUser(self):
        """ Test attributes value of a BaseModel instance """
        my_user = User()

        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.save()
        my_user_json = my_user.to_dict()

        self.assertEqual(my_user.first_name, my_user_json['first_name'])
        self.assertEqual(my_user.last_name, my_user_json['last_name'])
        self.assertEqual('email' not in my_user_json, True)
        self.assertEqual('password' not in my_user_json, True)
        self.assertEqual('User', my_user_json['__class__'])
        self.assertEqual(my_user.id, my_user_json['id'])

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.second_name = "Holberton"
        my_user.email = "betty@holberton.com"
        my_user.password = "root"
        my_user.save()
        first_dict = my_user.to_dict()

        my_user.first_name = "Second"
        my_user.save()
        sec_dict = my_user.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])
        self.assertNotEqual(first_dict['first_name'], sec_dict['first_name'])
        self.assertEqual(first_dict['second_name'], sec_dict['second_name'])
        self.assertEqual(first_dict['second_name'], sec_dict['second_name'])
        self.assertEqual(first_dict['email'], sec_dict['email'])
        self.assertEqual(first_dict['password'], sec_dict['password'])
