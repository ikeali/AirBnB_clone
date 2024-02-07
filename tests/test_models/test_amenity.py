import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage  # Make sure to import storage

class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        self.resetStorage()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}  # Assuming storage is a module with FileStorage
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]  # Assuming there is an attributes() method
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()

