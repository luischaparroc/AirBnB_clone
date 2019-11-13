#!/usr/bin/python3
"""
Unittest for review.py
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_review(unittest.TestCase):
    """Tests instances and methods from Review class"""
    def setUp(self):
        """sets variable everytime"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(Review())), res)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertEqual(issubclass(Review, BaseModel), True)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(Review, 'place_id'), True)
        self.assertEqual(hasattr(Review, 'user_id'), True)
        self.assertEqual(hasattr(Review, 'text'), True)
