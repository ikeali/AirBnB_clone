#!/usr/bin/python3
"""
Command interpreter for AirBnB project.
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

