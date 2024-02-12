import unittest
from models.base_model import BaseModel
from datetime import datetime
import json

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        obj = BaseModel()
        string_representation = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), string_representation)

    def test_save(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_with_custom_attributes(self):
        obj = BaseModel()
        obj.custom_attribute = 'test'
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['custom_attribute'], 'test')

    def test_init_with_parameters(self):
        obj_id = '123'
        created_at = '2022-01-01T12:00:00.000000'
        updated_at = '2022-01-02T14:30:00.000000'

        obj = BaseModel(id=obj_id, created_at=created_at, updated_at=updated_at)
        self.assertEqual(obj.id, obj_id)
        self.assertEqual(obj.created_at, datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.updated_at, datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

if __name__ == '__main__':
    unittest.main()

