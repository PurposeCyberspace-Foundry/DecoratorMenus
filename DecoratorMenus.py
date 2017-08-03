"""
DecoratorMenus
This class allows the use of @decorators to create submenu-driven programs easily and quickly in python
the menu_item options are all passed directly to the "add_submenu" argparse function
the argument options are passed to the "add_argument" argparse function
"""
import argparse
ap = argparse.ArgumentParser()
sp = ap.add_subparsers()
def menu_item(*args, **kwargs):
    # print "creating menu item"
    def argument_processor(func_or_arguments):
        if callable(func_or_arguments):  # the next item is the function
            f = func_or_arguments
            arguments = []
        else:
            f = func_or_arguments[0]
            arguments = func_or_arguments[1]

        sap = sp.add_parser(*args, **kwargs)
        sap.set_defaults(func=f)
        for argument in arguments:
            sap.add_argument(*argument[0], **argument[1])
        # return f
    return argument_processor

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

def run_menu():
    args = vars(ap.parse_args())
    func = args.pop("func")
    func(**args)
