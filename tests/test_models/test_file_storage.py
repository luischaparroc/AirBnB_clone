#!/usr/bin/python3
""" Module of Unittests """
import unittest
from unittest.mock import patch
from unittest import TestCase
from io import StringIO
from models.base_model import BaseModel
from models import storage


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        my_model = BaseModel()

        my_model.full_name = "BaseModel Instance"
        my_model.save()
        bm_dict = my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ Test save, reload and update functions """
        my_model = BaseModel()

        my_model.my_name = "First name"
        my_model.save()
        bm_dict = my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create1 = bm_dict['created_at']
        update1 = bm_dict['updated_at']

        my_model.my_name = "Second name"
        my_model.save()
        bm_dict = my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create2 = bm_dict['created_at']
        update2 = bm_dict['updated_at']

        self.assertEqual(create1, create2)
        self.assertNotEqual(update1, update2)
        self.assertEqual(bm_dict['my_name'], "Second name")
