#!/usr/bin/python3
'''program called console.py that contains the entry point
 of the command interpreter'''
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''command processor for hbnb
    Attributes:
        prompt(str): prompt for command line
    '''
    prompt = '(hbnb) '

    __class = ["BaseModel",
               "User",
               "State",
               "Place",
               "City",
               "Amenity",
               "Review"]

    def do_EOF(self, arg):
        '''Exit the program
        '''
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        '''when emptyline, do nothing
        '''
        pass

    def do_create(self, arg):
        '''create [BaseModel]
        create new instance of the class BaseModel
        Arguments:
        arg(str): arguments
        '''
        args = arg.split()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] in HBNBCommand.__class):
            instance = eval(args[0])()
            for kwargs in args[1:]:
                try:
                    key, value = kwargs.split("=", 1)
                    if (value.startswith('"')) and (value.endswith('"')):
                        value = value[1:-1]
                        value = value.replace("_", " ")
                        value = value.replace('\\"','"' )
                    elif "." in value:
                        value = float(value)
                    else:
                        value = int(value)
                    setattr(instance, key, value)
                except (TypeError, ValueError):
                    continue
            storage.save()
            print("{}".format(eval(args[0])().id))

        else:
            print("** class doesn't exist **")
                       

    def do_show(self, arg):
        ''' Prints the string representation of an instance
        based on the class name and id
        Arguments:
            arg(str): arguments
        '''
        args = arg.split()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class):
            print("** class doesn't exist **")
        elif (args[0] in HBNBCommand.__class) and len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
        Arguments:
            args(str): arguments
        '''
        args = arg.split()
        if (len(args) < 1):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class):
            print("** class doesn't exist **")
        elif (args[0] in HBNBCommand.__class) and len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based
        or not on the class name
        Arguments:
            arg(str): arguments
        '''
        if (arg in HBNBCommand.__class) or (not arg):
            list_inst = []
            for obj in storage.all().values():
                list_inst.append(obj.__str__())
            print(list_inst)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        '''Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding or
        updating attribute
        Arguments:
            arg(str): arguments
        '''
        pattern = r'"(.*?)"|\{(.*?)\}|\'(.*?)\'|\[(.*?)\]|(\S+)'
        matches = re.findall(pattern, arg)
        args = [group[0] or group[1] or group[2] or group[3] or group[4]
                for group in matches]
        if (len(args) == 0):
            print("** class name missing **")
            return False
        elif (args[0] not in HBNBCommand.__class):
            print("** class doesn't exist **")
            return False
        elif (args[0] in HBNBCommand.__class) and (len(args) == 1):
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return False
        elif (len(args) == 2):
            print("** attribute name missing **")
            return False
        elif (len(args) == 3):
            print("** value missing **")
            return False
        if (len(args) == 4):
            key = f"{args[0]}.{args[1]}"
            if (args[2] in
                    storage.all()[key].__class__.__dict__.keys()):
                valtype = type(storage.all()[key].__class__.__dict__[args[2]])
                storage.all()[key].__dict__[args[2]] = valtype(args[3])
            else:
                storage.all()[key].__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            for key, value in eval(args[2]).items():
                if (key in storage.all()[key].__class__.__dict__.keys() and
                        type(storage.all()[key].__class__.__dict__[key])
                        in {str, int, float}):
                    valtype = type(storage.all()[key].__class__.__dict__[key])
                    storage.all()[key].__dict__[key] = valtype(value)
                else:
                    storage.all()[key].__dict__[key] = value
        storage.save()

    def default(self, arg):
        '''Print all using the syntax <class name>.all()
        '''
        if '.' in arg:
            cls, args = arg.split('.', 1)
            if args == "all()":
                return self.do_all(cls)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
