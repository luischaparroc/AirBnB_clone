#!/usr/bin/python3
""" Module of Unittests """
import unittest
from unittest.mock import patch
from unittest import TestCase
from io import StringIO
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """
        my_model = BaseModel()

        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()

        self.assertEqual(my_model.name, my_model_json['name'])
        self.assertEqual(my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(my_model.id, my_model_json['id'])
