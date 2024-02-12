import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
import json

class TestBaseModel(unittest.TestCase):

    @patch('models.base_model.storage', None)  # Mock storage to prevent actual file operations
    def setUp(self):
        self.obj = BaseModel()
        self.obj.id = 'test_id'
        self.obj.created_at = self.obj.updated_at = datetime.now()

    @patch('models.base_model.storage', None)
    def tearDown(self):
        del self.obj

    def test_init(self):
        self.assertIsInstance(self.obj, BaseModel)
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_str(self):
        string_representation = "[BaseModel] (test_id) {}".format(self.obj.__dict__)
        self.assertEqual(str(self.obj), string_representation)

    @patch('models.base_model.storage', None)
    def test_save(self):
        initial_updated_at = self.obj.updated_at
        with patch('models.base_model.storage.save') as mock_save:
            self.obj.save()
            self.assertNotEqual(initial_updated_at, self.obj.updated_at)
            mock_save.assert_called_once()

    @patch('models.base_model.storage', None)
    def test_to_dict(self):
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.obj.updated_at.isoformat())

    @patch('models.base_model.storage', None)
    def test_to_dict_with_custom_attributes(self):
        self.obj.custom_attribute = 'test'
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict['custom_attribute'], 'test')

    def test_init_with_parameters(self):
        obj_id = '123'
        created_at = '2022-01-01T12:00:00.000000'
        updated_at = '2022-01-02T14:30:00.000000'

        with patch('models.base_model.storage.new') as mock_new:
            obj = BaseModel(id=obj_id, created_at=created_at, updated_at=updated_at)
            self.assertEqual(obj.id, obj_id)
            self.assertEqual(obj.created_at, datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
            self.assertEqual(obj.updated_at, datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))
            mock_new.assert_called_once()

if __name__ == '__main__':
    unittest.main()

