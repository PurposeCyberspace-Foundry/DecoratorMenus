"""
DecoratorMenus
This class allows the use of @decorators to create submenu-driven programs easily and quickly in python
the menu_item options are all passed directly to the "add_submenu" argparse function
the argument options are passed to the "add_argument" argparse function

for example use, see example.py
"""
import argparse
from ExceptionHiding import hide_last_exception


# this could be replaced in the future to accept @argument decorators and
# provide default arguments for the program
ap = argparse.ArgumentParser()

# this could be replaced in the future as well, with another @function to create
# logical command groups
sp = ap.add_subparsers()

# this will register a function or a function with arguments as a menu command
# it returns the function with the actiongroup attached, so theoretically you
# can do more with the actiongroup, probably using normal argparse routines
def menu_item(*args, **kwargs):
    def next_item_processor(func):
        # no command name provided. no problem.
        command = args
        if not command:
            command = [func.__name__.replace("_","-")]
        parser_action = sp.add_parser(*command, **kwargs)
        parser_action.set_defaults(func=func)
        if hasattr(func, 'arguments'):
            for argument in func.arguments:
                parser_action._add_action(argument)
        func.action_group = parser_action
        return func
    return next_item_processor

# this will add an argument to the function. It doesn't do anything on its own,
# but must follow menu_item
def argument(*args, **kwargs):
    def next_item_processor(func):
        # create an action from an ephemeral ArgumentParser
        action = argparse.ArgumentParser().add_argument(*args, **kwargs)

        # make sure that each action has a valid varname parameter to match to
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

# parses the args then runs the associated function passing it the
# named args as parameters
def run_menu():
    args = vars(ap.parse_args())
    func = args.pop("func")
    func(**args)
