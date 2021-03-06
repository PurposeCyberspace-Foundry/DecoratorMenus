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
