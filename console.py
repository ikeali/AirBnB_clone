#!/usr/bin/python3
"""
Command interpreter for AirBnB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class definition for command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program.
        """
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
        else:
            class_name = args.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[class_name]()
                new_instance.save()
                print(new_instance.id)
    
    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        arguments = split(args)
        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            instances = storage.all()
            print(instances.get(key, "** no instance found **"))

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        arguments = split(args)
        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, line):
        """Prints all string representation of all instances or instances of a class."""
        words = line.split(' ')

        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            if len(words) > 1:
                key_list = ["{}.{}".format(words[0], obj.id) for obj in storage.all().values() if type(obj).__name__ == words[0]]
            else:
                key_list = ["{}.{}".format(type(obj).__name__, obj.id) for obj in storage.all().values()]

            print([str(storage.all()[key]) for key in key_list])



    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arguments = args.split()
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attribute_name = arguments[2]
                attribute_value = arguments[3].strip('"')
                setattr(obj, attribute_name, attribute_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

