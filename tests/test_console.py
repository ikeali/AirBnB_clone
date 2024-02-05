import unittest
from unittest.mock import patch
from io import StringIO
import os
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console_output = StringIO()

    def tearDown(self):
        self.console_output.close()

    def test_create(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(len(self.console_output.getvalue()) > 0)
        self.assertEqual(type(storage.all()["BaseModel." + self.console_output.getvalue().strip()]), BaseModel)

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
        self.assertTrue(len(self.console_output.getvalue()) > 0)

    def test_show_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_show_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show BaseModel 1234")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
        self.assertEqual(storage.all().get("BaseModel." + obj_id, None), None)

    def test_destroy_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_destroy_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_destroy_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy BaseModel 1234")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_all(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("all")
        self.assertTrue(len(self.console_output.getvalue()) > 0)

    def test_all_with_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("all BaseModel")
        self.assertTrue(len(self.console_output.getvalue()) > 0)

    def test_all_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("all InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update BaseModel {} name 'new_name'".format(obj_id))
        obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(obj.name, 'new_name')

    def test_update_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update InvalidClass 1234 name 'new_name'")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_update_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update BaseModel name 'new_name'")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_update_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update BaseModel 1234 name 'new_name'")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_update_missing_attr_name(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update BaseModel 1234")
        self.assertEqual("** attribute name missing **\n", self.console_output.getvalue())

    def test_update_missing_value(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update BaseModel 1234 name")
        self.assertEqual("** value missing **\n", self.console_output.getvalue())

    def test_count(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("count BaseModel")
        self.assertEqual("0\n", self.console_output.getvalue())

    def test_count_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("count InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_show_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show_id BaseModel {}".format(obj_id))
        self.assertTrue(len(self.console_output.getvalue()) > 0)

    def test_show_id_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show_id InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_show_id_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show_id BaseModel")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_show_id_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("show_id BaseModel 1234")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_destroy_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy_id BaseModel {}".format(obj_id))
        self.assertEqual(storage.all().get("BaseModel." + obj_id, None), None)

    def test_destroy_id_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy_id InvalidClass")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_destroy_id_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy_id BaseModel")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_destroy_id_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("destroy_id BaseModel 1234")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_update_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel {} name 'new_name'".format(obj_id))
        obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(obj.name, 'new_name')

    def test_update_id_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id InvalidClass 1234 name 'new_name'")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_update_id_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel name 'new_name'")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_update_id_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234 name 'new_name'")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_update_id_missing_attr_name(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234")
        self.assertEqual("** attribute name missing **\n", self.console_output.getvalue())

    def test_update_id_missing_value(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234 name")
        self.assertEqual("** value missing **\n", self.console_output.getvalue())

    def test_update_id_with_dict(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("create BaseModel")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel {} {{'name': 'new_name', 'age': 25}}".format(obj_id))
        obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(obj.name, 'new_name')
        self.assertEqual(obj.age, 25)

    def test_update_id_with_dict_invalid_class(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id InvalidClass 1234 {{'name': 'new_name', 'age': 25}}")
        self.assertEqual("** class doesn't exist **\n", self.console_output.getvalue())

    def test_update_id_with_dict_missing_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel {{'name': 'new_name', 'age': 25}}")
        self.assertEqual("** instance id missing **\n", self.console_output.getvalue())

    def test_update_id_with_dict_invalid_id(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234 {{'name': 'new_name', 'age': 25}}")
        self.assertEqual("** no instance found **\n", self.console_output.getvalue())

    def test_update_id_with_dict_missing_dict(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234")
        self.assertEqual("** dictionary missing **\n", self.console_output.getvalue())

    def test_update_id_with_dict_invalid_dict(self):
        with patch('sys.stdout', new=self.console_output):
            HBNBCommand().onecmd("update_id BaseModel 1234 {'name': 'new_name', 'age': 25}")
        self.assertEqual("** invalid dictionary **\n", self.console_output.getvalue())


if __name__ == "__main__":
    unittest.main()

