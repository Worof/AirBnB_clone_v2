#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax"""
        if '.' in line and '(' in line and ')' in line:
            try:
                cls, method = line.split(".", 1)
                method_name = method.split("(", 1)[0]
                args = method.split("(", 1)[1].split(")", 1)[0]
                args = args.replace(",", "").split()
                new_line = method_name + " " + cls + " " + " ".join(args)
                return new_line
            except:
                pass
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        exit()

    def emptyline(self):
        """Overwrites the emptyline method from CMD"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        args = arg.split(" ")
        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.classes:
            new_instance = HBNBCommand.classes[args[0]]()
            for attr in args[1:]:
                key, value = attr.split("=")
                value = self.parse_value(value)
                if value is not None:
                    setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def parse_value(self, value):
        """Parses the value from string to correct Python data type"""
        if value[0] == '"' and value[-1] == '"':
            return value.strip('"').replace('_', ' ').replace('\"', '"')
        elif '.' in value:
            try:
                return float(value)
            except ValueError:
                return None
        else:
            try:
                return int(value)
            except ValueError:
                return None

    def do_show(self, arg):
        """Shows an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances of a class or all instances in storage if no class is specified"""
        args = arg.split()
        obj_list = []
        obj_dict = storage.all()
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, obj in obj_dict.items():
            if len(args) > 0 and args[0] == obj.__class__.__name__:
                obj_list.append(str(obj))
            elif len(args) == 0:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name, id, attribute name, and attribute value"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            obj = obj_dict[key]
            setattr(obj, args[2], args[3])
            obj.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        count = 0
        obj_dict = storage.all()
        for key in obj_dict:
            if args[0] == key.split(".")[0]:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
