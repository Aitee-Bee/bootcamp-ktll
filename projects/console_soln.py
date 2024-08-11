#!/usr/bin/python3
"""
A module to be used a command prompt for
the running the entire application
"""
import cmd


class AirBNBCommand(cmd.Cmd):
    """
    The cmd is a Python module for creating a program
    that serve as a command line interpreter.
    """
    intro = "Welcome to the AirBNB command program"
    prompt = "airbnb >>> "

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        exit()
    
    def do_emptyline(self, line):
        pass

if __name__ == "__main__":
    AirBNBCommand().cmdloop()
