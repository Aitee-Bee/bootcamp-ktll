"""
ERRORS - SYNTAX ERROR
------------------------------------------------------
An error is an issue or a problem in a program that stops
the program from completing a particular task. Errors
happens during the parsing of the script in Python.
They can result from incorrect syntax such as missing
closing quote, parenthesis.

EXCEPTIONS
------------------------------------------------------
Exceptions are also called logical errors. Exceptions
occur during runtime and they can be caught by the
program and handled to avoid the program from crashing.
They are unanticipated events that stops the program from
running.

DIFFERENT TYPES OF ERRORS
-----------------------------------------------------
1. Syntax Error: occurs when Python cannot understand
the code you have written.
2. Name Error: occurs when variable or function name
is used or called without being initially defined.
3. TypeError: occurs when an incompatible data type
is passed to a function.
4. Value Error: occurs when a value is not the expected
value in an operation.
5. Index Error: occurs when Pyhton has gone out of the
range of index available to it.
"""
# print('I'm a boy') syntax error
# print(color) name error
# 'python'.index(2) type error

# Exceptions
# We can have an exception if we are trying to open a file that does not exit
# file = open('learn.txt')
# We try to divide an integer by zero
# ans = 89 / 0
# We try to import a module that does not exist
# import learn

"""
RAISING AN EXCEPTION
---------------------------------------------------------
You can raise an exception useing the raise key word
"""
age = 0
# if age == 0:
#     # raise Exception("Your cannot use an age of 0")
#     raise ZeroDivisionError("Your cannot use an age of 0")

amount = 500
# if amount < 400:
#     raise Exception("Your balance is not enough")

"""
CATCHING AN EXCEPTION
---------------------------------------------------------
You can catch an anticipated exception using the try, except,
else, finally block in Python.

try block lets you implement code that may likely have an error
except block lets you handle the error
else block lets you execute code when there is no error
finally block lets you excute code regardless of the result of  try and except block
"""
# fav_num = input("Type your favorite number: ")
# try:
#     print(4 / int(fav_num))
# except ZeroDivisionError:
#     print("Error: you cannot use zero")

try:
    file = open('learn.txt')
    print("The file has opened")
    # file.seek()
    file.close()
except FileNotFoundError:
    print("Error: The file is not found")
except ValueError:
    print("Value not valid")
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception:
    print("Error: problem with file openning.")
finally:
    file.close()
    print('File operation ended.')

# try:
#     file = open('learn.txt')
# except Exception:
#     print("Error: The file is not found")

print('The file did not stop executing')
