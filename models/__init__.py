#!/usr/bin/python3
""" Import modules and packages """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

l_classes = ['BaseModel', 'User', 'Amenity',
             'Place', 'City', 'State', 'Review']
