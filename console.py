#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_create(self, type_model):
        """ Creates an instance according to a given class """
        l_classes = ['BaseModel', 'User', 'Amenity',
                     'Place', 'City', 'State', 'Review']

        if not type_model:
            print("** class name missing **")
        elif type_model not in l_classes:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """
        l_classes = ['BaseModel', 'User', 'Amenity',
                     'Place', 'City', 'State', 'Review']

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1]:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
