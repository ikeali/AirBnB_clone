#!/usr/bin/python3
"""Command interpreter module"""

import cmd
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
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
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        arguments = shlex.split(args)
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[arguments[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        arguments = shlex.split(args)
        instances = storage.all()

        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in instances:
            print("** no instance found **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            print(instances[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        arguments = shlex.split(args)
        instances = storage.all()

        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in instances:
            print("** no instance found **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            del instances[key]
            storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        arguments = shlex.split(args)
        instances = storage.all()

        if not args:
            print([str(value) for value in instances.values()])
        elif arguments[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in instances.items() if key.startswith(arguments[0])])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arguments = shlex.split(args)
        instances = storage.all()

        if not arguments or arguments[0] not in storage.classes():
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in instances:
            print("** no instance found **")
        elif len(arguments) < 3:
            print("** attribute name missing **")
        elif len(arguments) < 4:
            print("** value missing **")
        elif len(arguments) > 4:
            print("Too many arguments")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            obj = instances[key]

            attr_name = arguments[2]
            if hasattr(obj, attr_name):
                attr_value = arguments[3].strip('"')
                try:
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                    obj.save()
                except Exception:
                    print("Invalid value type")
            else:
                print("Attribute name not found")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

