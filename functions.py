"""
# FUNCTIONS - 07-04-2024
---------------------------------------------------------
A function is a construct that allows you to group related
lines of code into a single unit.

You use the `def` keyword to define a function.
Python has some inbuilt functions as well.
Every function may have `return` a value or Python will return None implicitly.

Function takes arguments inside the ().
"""
def functionane(arguments):
    return 1

"""
# Function - 14-04-2024
---------------------------------------------------------
There are user defined functions and in-built functions in Python.
To define a function you use `def` keyword.
A function must do one thing only.
A function takes one or more arguments but it is best to keep the number
of arguments in python below 5.
There are two types of arguments in python:
    positional arguments (*args) *members
        A positional argument means that when the function is being called or used
        Python identifies the arguments based on the positions of each argument.
    keyword arguments (**kwargs) **members
        A keyword argument means that when the function is being called or used
        Python identifies the arguments using keywords. Thus, you may choose to
        change the positions of arguments.
"""
# Example - user define functions
def print_first_name(first_name):
    print(first_name)

# How to use the function defined above
my_first_name = "john"
print_first_name(my_first_name)  # we are now calling the function with one argument

def print_first_name_with_return(first_name):
    return first_name

result = print_first_name_with_return(my_first_name)
print(result)

print(print_first_name_with_return(my_first_name))

"""
# CLASSWORK
--------------------------------------------------------------------
Write a function that takes two arguments, your first name and last name then prints your full name.
Write another function that takes two arguments, your first name and last name then returns your full name.
"""
# Solution
def print_full_name(first_name, last_name):
    print(first_name + " " + last_name)

def print_full_name_with_return(first_name, last_name):
    return first_name + " " + last_name

print_full_name("john", 'doe')
print_full_name("doe", 'john')  # positional argument
print_full_name(last_name="doe", first_name='john')  # keyword argument
print(print_full_name_with_return("john", "doe"))


def family(*args): # args is a tuple ('red', 'black', 'orange'), list ['red', 'black', 'orange']
    for arg in args:
        print(arg, end=' ')
    print()

family("uduak", "itoro", "emem", "ima-abasi")

def family_details(**kwargs): # kwargs is a dictionary {key=value} {'name'='john doe', 'age'=14, 'gender'='male}
    for key, value in kwargs.items(): # items() is a dictionary function that gives us both the key and value of each item in a dictionary
        print(key + "=" + str(value))
    
family_details(name='john doe', age=14, gender='male')

"""
# CLASSWORK
----------------------------------------------------------------
Write a function that asks a user for his first name and then his last name and print
last name before first name.
"""
