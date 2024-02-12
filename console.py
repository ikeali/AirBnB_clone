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
            try:
                new_instance = eval(args + "()")
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

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

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        arguments = split(args)
        instances = storage.all()

        if not args:
            print([str(value) for value in instances.values()])
        elif arguments[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in instances.items() if key.startswith(arguments[0])])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arguments = split(args)

        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            else:
                instance = instances[key]
                attr_name = arguments[2]
                attr_value = arguments[3].strip('"')

                if hasattr(instance, attr_name):
                    attr_type = type(getattr(instance, attr_name))
                    try:
                        setattr(instance, attr_name, attr_type(attr_value))
                        instance.save()
                    except (ValueError, TypeError):
                        print("** invalid value **")
                else:
                    print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

