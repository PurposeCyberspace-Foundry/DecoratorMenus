"""
DecoratorMenus
This class allows the use of @decorators to create submenu-driven programs easily and quickly in python
the menu_item options are all passed directly to the "add_submenu" argparse function
the argument options are passed to the "add_argument" argparse function

for example use, see example.py
"""
import argparse
from ExceptionHiding import hide_last_exception


# this could be replaced in the future to accept @argument decorators and provide default arguments for the program
ap = argparse.ArgumentParser()

# this could be replaced in the future as well, with another @function to create logical command groups
sp = ap.add_subparsers()

# this will register a function or a function with arguments as a menu command
# it would be really cool to have menu_item return a menu_item class which then could be added by the above
# hypothetical future decorators
def menu_item(*args, **kwargs):
    def next_item_processor(func):
        sap = sp.add_parser(*args, **kwargs)
        sap.set_defaults(func=func)
        if hasattr(func, 'arguments'):
            for argument in func.arguments:
                #print "added {} to {}".format((argument.args, argument.kwargs), func.__name__)
                sap._add_action(argument)

        return sap
        # one could concievably return the function, in which case the function would actually be defined
        # for now, the function goes away once it is wrapped like this and the definition remains empty.
        # return f
    return next_item_processor

# this will add an argument to the function. It doesn't do anything on its own, but must follow menu_item
def argument(*args, **kwargs):
    def next_item_processor(func):
        # create an action from an ephemeral ArgumentParser
        action = argparse.ArgumentParser().add_argument(*args, **kwargs)

        #make sure that each action has a valid varname target
        if action.dest not in func.__code__.co_varnames:
            hide_last_exception()
            raise AttributeError(
                    '"{.dest}" not an argument for {.__name__}{}'\
                      .format(action, func,
                        str(func.__code__.co_varnames).replace('\'','')))

        # if the function has an "arguments" list, add to it, otherwise
        # start a new list
        func.__dict__.setdefault('arguments',[])
        func.arguments.append(action)

        # pass the func to the next higher level
        return func

    return next_item_processor

# parses the args then runs the associated function passing it the named args as parameters
def run_menu():
    args = vars(ap.parse_args())
    func = args.pop("func")
    func(**args)
