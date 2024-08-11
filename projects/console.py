import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "hbnb"


def quit(self):
    return True


def EOF(self):
    return True


def emptyline(self):
    pass
