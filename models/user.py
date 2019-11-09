#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for User"""
        super().__init__(**kwargs)
