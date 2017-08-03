#DecoratorMenus
"""
The MIT License

Copyright 2017 Matthew Lombardo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
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