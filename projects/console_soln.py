#!/usr/bin/python3
"""
A module to be used a command prompt for
the running the entire application
"""
import cmd
from shlex import split
import models
from models.base_model_soln import BaseModel


class AirBNBCommand(cmd.Cmd):
    """
    The cmd is a Python module for creating a program
    that serve as a command line interpreter.
    """
    intro = "Welcome to the AirBNB command program"
    prompt = "(airbnb) >>> "
    __classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        exit()
    
    def do_emptyline(self, line):
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, save it, and print id."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            # kwargs = {}
            # for i in range(1, len(args)):
            #     key, value = tuple(args[i].split("="))
            #     if value[0] == '"':
            #         value = value.strip('"').replace("_", " ")
            #     else:
            #         try:
            #             value = eval(value)
            #         except (SyntaxError, NameError):
            #             continue
            #     kwargs[key] = value
            # obj = eval(args[0])(**kwargs)
            # obj.save()
            # print(obj.id)
            new_instance = AirBNBCommand.__classes[args[0]]()
            models.storage.save()
            print(new_instance)
            # models.storage.save()
    
    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objs = models.storage.all()
            if key in objs:
                print(key)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on classname and id."""
        args = split(line, " ")
        if not line:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objs = models.storage.all()
            if key in objs:
                del objs[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print all string representation of instance."""
        try:
            args = split(line, " ")
            if args[0] not in self.__classes:
                raise NameError()
            
            obj = models.storage.all(eval(args[0]))
            for key in obj:
                print(obj[key].__str__())
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objs = models.storage.all()
            if key in objs:
                obj = objs[key]
                atrr_name = args[2]
                attr_value = args[3]
                setattr(obj, atrr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    AirBNBCommand().cmdloop()
