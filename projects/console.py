#!/usr/bin/python3
"""
A module to be used a command prompt for
the running the entire application
"""
import cmd
from . import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City


class AirBNBCommand(cmd.Cmd):
    """
    The cmd is a Python module for creating a program
    that serve as a command line interpreter.
    """

    intro = "Welcome to the AirBNB command program"
    prompt = "airbnb >>> "
    classes = ["BaseModel"]

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        exit()

    def do_emptyline(self, line):
        pass

    def do_create(self, line):
        if not line:
            print("**class name missing")
        elif line not in self.classes:
            print("**class does not exist**")
        else:
            new_instance = BaseModel()  # creates a new instance of the BM
            new_instance.save()  # call the save method of F.S to save the new instance to storage
            print(new_instance.id)

    def do_show(self, line):
        m = line.split(" ")  # split at the first instance of the space
        if len(m) == 0:  # class name not entered
            print("**class name missing")
        elif (m[0] not in self.classes):  # the first argument passed after we enter show not in the class attribute
            print("**class does not exist**")
        elif len(m) == 1: # if the length is 1, only just class name provided, id aint among
            print('**instance id missing')
        else:
            objects = storage.all()
            if m[0] + '.' + m[1] not in objects:
                key = m[0] + '.' + m[1]  #Classname and id 
                print(objects[key])
            else:
                print('No instance found')

    def destroy
       

    
    
        

            

    









if __name__ == "__main__":
    AirBNBCommand().cmdloop()
