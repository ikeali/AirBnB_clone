#!/usr/bin/python3
"""
class City
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ class that inherits from BaseModel """
    state_id = ""
    name = ""
