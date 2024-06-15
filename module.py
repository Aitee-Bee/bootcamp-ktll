"""
MODULE
---------------------------------------------------
A module is a file with the .py extension.
You can import a module into another file and all the
variables, functions and classes will be available in the
file for you to use.

PACKAGE
-----------------------------------------------------
A package is a folder containing modules and a special
file called __init__.py
"""
import import_module

print(import_module.cap_color())

import import_module as im # `as` is use to create an alias for the module we are importing
print(im.cap_color())

from import_module import cap_color
print(cap_color())

def tell_us_your_food():
    print("my food is", im.food)

tell_us_your_food()

from package import color
color.cap_color()
