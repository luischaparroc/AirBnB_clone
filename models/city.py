#!/usr/bin/python3
"""
Defines city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""
    state_id = ""
    name = ""
