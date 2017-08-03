# DecoratorMenus
Use python @decorators to create command line menus

## How to use:
After including DecoratorMenus 
* use the `@menu_item` to add sub-commands to your main program
* use the `@argument` to create arguments specific to that sub-command
* use the `run_menu()` command to display the menu and parse any command line arguments
## Example Code
````
# This code is available in example.py

from DecoratorMenus import *

# Menu Item 1
@menu_item("do-func", help="I am a function that does something")
@argument('-l', '--list', dest="item_list", nargs="+", help="print a list")
@argument('-p', '--python', action="store_true", help="I like python")
def func(item_list, python):
    if python:
        print "I like python, too"

    if item_list:
        print "here's your list"
        print item_list

# Menu Item 2
@menu_item("second-func", help="I'm another option")
@argument('-f', '--force', action="store_true", help="Try harder")
def func(force):
    if not force :
        print "you're not trying hard enough"

    else:
        print "yay, you did it"

if __name__=="__main__":
    run_menu()
```
