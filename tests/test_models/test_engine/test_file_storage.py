#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json
import datetime


class FileStorageTests(unittest.TestCase):
    """ Suite of File Storage Tests """

    def setUp(self):
        """ Method invoked for each test """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path) is True:
            os.remove(storage._FileStorage__file_path)

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

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

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """verify if JSON exists"""
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """test if reload """
        self.assertFalse(os.path.exists(storage._FileStorage__file_path))
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testnew(self):
        """test if new is working"""
        self.assertFalse(os.path.exists(storage._FileStorage__file_path))
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            for key, value in json.load(f).items():
                storage.new(BaseModel(**value))
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ Check save self """
        self.assertFalse(os.path.exists(storage._FileStorage__file_path))

        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def testHasAttributes(self):
        """ Test Attributes """
        my_model = BaseModel()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def testType(self):
        """ Check type objects """
        my_model = BaseModel()

        my_model.save()

        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)

        dict_model = my_model.to_dict()
        self.assertIsInstance(dict_model, dict)

if __name__ == '__main__':
    unittest.main()
