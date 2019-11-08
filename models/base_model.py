#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """initializes all attributes
        """
        if not kwargs:
            self.name = ""
            self.my_number = 0
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.name = kwargs['name']
            self.my_number = kwargs['my_number']
            self.id = kwargs['id']
            f = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(kwargs['created_at'], f)
            self.updated_at = datetime.strptime(kwargs['updated_at'], f)

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        return class_name + " (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datemtimes converted to strings
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
