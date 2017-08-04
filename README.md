# DecoratorMenus
Use python @decorators to create command line menus with a cleaner syntax, but the same powerful options as python's own [`argparse`](https://docs.python.org/3/library/argparse.html)

## How to use:
After including `DecoratorMenus` in your file
* use the `@menu_item` to add sub-commands to your main program
* use the `@argument` to create arguments specific to that sub-command
* the function that follows will be called automatically when the appropriate menu item is typed from the command line
* use the `run_menu()` command to display the menu and parse any command line arguments
## Example Code
An example is worth 1000 words...
```
# This code is available in example.py

"""
A short example of DecoratorMenus
"""
from DecoratorMenus import *


# Menu Item 1
# a menu_item is a tier-2 command

@menu_item("try-it", help="I am a function that does something")
# each argument must match a function argument
@argument('-l', '--list', dest="item_list", nargs="+", help="print a list")
@argument('-p', '--python', action="store_true", help="I like python")
# this must have parameters as indicated in the @argument(s)
def like_or_list(item_list, python):
    if python:
        print "I like python, too"

    if item_list:
        print "here's your list"
        print item_list

    if not (python or item_list):
        print "ok, you tried"

# Menu Item 2
# here the name of the command is inferred from the function name
@menu_item(help="I'm another option")
@argument('-f', '--force', action="store_true", help="Try harder")
def try_again(force):
    if not force :
        print "you're not trying hard enough"

    else:
        print "yay, you did it"

if __name__=="__main__":
    run_menu()

```

## Example Output
The user can obtain help on your program using the -h flag. e.g.
```
> python example.py -h
```
```
usage: example.py [-h] {do-func,second-func} ...

positional arguments:
  {do-func,second-func}
    do-func             I am a function that does something
    second-func         I'm another option

optional arguments:
  -h, --help            show this help message and exit
```
Subcommands can similarly use the help flag
```
> python example.py second-func -h
```
```
usage: example.py second-func [-h] [-f]

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  Try harder
```
