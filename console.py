#!/usr/bin/python3
"""
Module documentation for console.py
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        args = shlex.split(line)
        if not args or args[0] not in storage.classes:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if hasattr(storage.classes[class_name], 'all'):
                print([str(obj) for obj in storage.classes[class_name].all()])
            else:
                print([str(obj) for key, obj in storage.all().items() if key.startswith(class_name)])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    obj = storage.all()[key]
                    try:
                        attribute_value = eval(attribute_value)
                    except:
                        pass
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()

    def do_count(self, line):
        """
        Retrieves the number of instances of a class.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                instances_count = len(storage.classes[class_name].all())
                print(instances_count)

    def do_show_id(self, line):
        """
        Retrieves an instance based on its ID.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy_id(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_update_id(self, line):
        """
        Updates an instance based on the class name and id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_dict = shlex.split(args[3])
                    obj = storage.all()[key]
                    for item in attr_dict:
                        k, v = item.split('=')
                        try:
                            v = eval(v)
                        except:
                            pass
                        setattr(obj, k, v)
                    obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

