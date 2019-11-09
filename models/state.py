#!/usr/bin/python3
"""
Class that defines a state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """class to create a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for state"""
        super().__init__(**kwargs)
