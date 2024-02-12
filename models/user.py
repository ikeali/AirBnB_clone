"""
class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ initializes class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
