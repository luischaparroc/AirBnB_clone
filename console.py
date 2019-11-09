#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models import l_classes


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_create(self, type_model):
        """ Creates an instance according to a given class """

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

    def do_destroy(self, arg):
        """ Deletes an instance passed """

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
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

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
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
