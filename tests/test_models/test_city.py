#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Tests instances and methods from city class"""

    c = City()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.c, City)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
