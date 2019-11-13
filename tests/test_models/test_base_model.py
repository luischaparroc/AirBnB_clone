#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class BaseModelTests(unittest.TestCase):
    """ Suite of Console Tests """

    def setUp(self):
        """Method invoked for each test"""
        if os.path.exists(storage._FileStorage__file_path) is True:
            os.remove(storage._FileStorage__file_path)

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

    def testSave(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        my_model = BaseModel()
        my_model.first_name = "First"
        my_model.save()
        first_dict = my_model.to_dict()

        my_model.first_name = "Second"
        my_model.save()
        sec_dict = my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

    def test_inst_storage(self):
        """test if storage is an instance of FileStorage"""
        self.assertEqual(isinstance(storage, FileStorage), True)

if __name__ == '__main__':
    unittest.main()
