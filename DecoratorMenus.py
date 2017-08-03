"""
DecoratorMenus
This class allows the use of @decorators to create submenu-driven programs easily and quickly in python
the menu_item options are all passed directly to the "add_submenu" argparse function
the argument options are passed to the "add_argument" argparse function

for example use, see example.py
"""
import argparse


# this could be replaced in the future to accept @argument decorators and provide default arguments for the program
ap = argparse.ArgumentParser()

# this could be replaced in the future as well, with another @function to create logical command groups
sp = ap.add_subparsers()

# this will register a function or a function with arguments as a menu command
# it would be really cool to have menu_item return a menu_item class which then could be added by the above
# hypothetical future decorators
def menu_item(*args, **kwargs):
    def argument_processor(func_or_arguments):
        if callable(func_or_arguments):  # the next item is the function, no arguments present
            f = func_or_arguments
            arguments = []
        else:
            f = func_or_arguments[0]
            arguments = func_or_arguments[1]

        # add a parser for this menu item
        sap = sp.add_parser(*args, **kwargs)
        sap.set_defaults(func=f)
        for argument in arguments:
            sap.add_argument(*argument[0], **argument[1])
            
        # one could concievably return the function, in which case the function would actually be defined
        # for now, the function goes away once it is wrapped like this and the definition remains empty.
        # return f
    return argument_processor

# this will add an argument to the function. It doesn't do anything on its own, but must follow menu_item
# again, in the future we could make this return something other than a tuple, like a class, for more robust
# arg creation
def argument(*args, **kwargs):
    def next_item_processor(func_or_arguments):
        
        if callable(func_or_arguments):  # the next item is the function
            f = func_or_arguments
            return f, [(args, kwargs)]
        else:
            # return the function, then add our arguments to the arglist
            f = func_or_arguments[0]
            rest = func_or_arguments[1]
            return f, rest + [(args, kwargs)]
    return next_item_processor

# parses the args then runs the associated function passing it the named args as parameters
def run_menu():
    args = vars(ap.parse_args())
    func = args.pop("func")
    func(**args)
