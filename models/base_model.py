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
            self.id = str(uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()
            models.storage.new(self)

    def __str__(self):
        """ __str__ function """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates public instance attribute """
        self.updated_at = date.now()
        models.storage.save

    def to_dict(self):
        """ returns dictionary containing all keys/values """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
