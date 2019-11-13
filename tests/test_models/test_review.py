#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    r = Review()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), res)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.r, Review)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)
