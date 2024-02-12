#!/usr/bin/python3
"""
class BaseModel
"""
import models
from uuid import uuid4
from datetime import date


class BaseModel:
    """ Defines all common attributes/methods for
    other classes """

    def __init__(self, *args, **kwargs):
        """ initializes class """
        if len(kwargs) > 0:
            for key, value in kwargs.items:
                if key == "created_at" or key == "updated_at":
                    value = date.time.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:

