#!/usr/bin/python3
"""
Defines city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for city"""
        super().__init__(**kwargs)
