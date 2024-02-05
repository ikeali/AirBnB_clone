#!/usr/bin/python3
"""Module documentation for FileStorage class."""
import json
from os.path import isfile
from models.user import User

class FileStorage:
     """
    Class to serialize instances to a JSON file and deserialize JSON file to instances.
    """
    classes = {
        'BaseModel': BaseModel,
        'User': User,  # Add User to the classes dictionary
        'State': State,  # Add State to the classes dictionary
        'City': City,    # Add City to the classes dictionary
        'Amenity': Amenity,  # Add Amenity to the classes dictionary
        'Place': Place,  # Add Place to the classes dictionary
        'Review': Review  # Add Review to the classes dictionary

        
        }
    """Class to serialize instances to a JSON file and deserialize JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj


