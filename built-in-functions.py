"""
You want to ask a user for a name.
Change the name to upper case letters.
Add a greeting to the name.
And then ask the person, if he wants to continue.
"""
# name = input('Type your name here: ')
# name = name.upper()
# "Hello " + name
# "Do you want to continue?"

def greetings():
    name = input('Type your name here: ')
    name = name.upper()
    print("Hello " + name)
    print("Do you want to continue?")

# greetings()
# greetings()

def age_check(age, name):
    if age < 18:
        return "Hello "  + name + " you are qualified!"
        print("Done")
    else:
        return "Hello " + name + " your are unqualified!"

# result = age_check(15, 'ima')
# result = age_check(name='ima', age=15)
# print(result)

def var_number_of_argument_function(*args):
    for arg in args:
        print(arg)
    return "Done"

res = var_number_of_argument_function('wilson', 89, 'js1', 'male')
print(res)

"""
# parameters - are defined when you are creating the function
# arguments - are the values you provide when you are calling the function
# *args - this is when you would want your function to accepts any number of positional arguments
# **kwargs - this is when you want your function to accept any number of keyword arguments
"""

"""
# LAMBDA FUNCTION
The lambda function is used to write anonymous functions in python program.
When you have a need to use a function but you don't want to first of all
define the function before using it, you may need to write a lambda function.
A lambda function cannot be used in more than one place.
Using the lambda function is a quick way of writing functions on the fly.
"""
def raise_to_power_2(number):
    return number ** 2

ret = raise_to_power_2(4)
print(type(ret))

rest = lambda number: number ** 2
print(type(rest))
print(rest(4))

multilpy = lambda x, y: x*y
print(multilpy(7,1))

colors = ['red', 'white', 'blue', 'brown', 'black', 'cyan']
"""
Write a program that returns a list with the colors in upper case letters.
"""
def capital_letters(word):
    return word.upper()

print([color.upper() for color in colors])
print([capital_letters(color) for color in colors])

print([(lambda color: color.upper())(color) for color in colors])

magic_nums = [12, 6, 3, 16, 21, 5]
[(lambda num: num**2)(num) for num in magic_nums]

"""
# MAP FUNCTION
------------------------------------------------------------------
This is a built in function that takes two arguments, a function
and an iterable. It applies each element of an iterable to a function.
"""
# map(func, iterable)
reslt = map(lambda num: num**2, magic_nums)
print(type(reslt))
print(list(reslt))

col = list(map(str.upper, colors))
print(col)

"""
ZIP FUNCTION
-------------------------------------------------------------------
The zip function takes a number of a iterables and returns a tuple containing
each element of the iterables.
"""
# zip(*iterable)
# index = [1, 2, 3, 4, 5, 6]
zip_colors = list(zip(range(len(colors)), colors, range(6), [0,1,2,3,4,5]))
print(type(zip(colors)))
print(zip_colors)


[0,1,2,3,4,5]
['red', 'white', 'blue', 'brown', 'black', 'cyan']
[0,1,2,3,4,5]

"""
# ENUMERATE FUNCTION
---------------------------------------------------------------------
A built in function that takes an iterable and returns a tuple of
the index and each of the elements of the iterable.
"""
print(list(enumerate(colors)))


# --------------------------------------------------------------------
# 12-May-2024
# --------------------------------------------------------------------
"""
# CLASSWORK
----------------------------------------------------------------------
Write a function that raises a number to the 5th power using the
lambda function.

Write a program that creates a tuple of a number and the square of the
number using a combination of a built-in function and a lambda function
Use this list of numbers:
numbers = [48, 16, 37, 4, 12, 2]

Using only a for loop and a lambda function, write a program that returns
every element of a list raised to itself.
Use this list:
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# 1 - solution
fifth_power = lambda num: num ** 5
print(type(fifth_power))
fifth_res = fifth_power(2)
print(fifth_res)

# 2 - solution
numbers = [48, 16, 37, 4, 12, 2]
lambda_power2 = list(zip(map(lambda x: x**2, numbers), numbers))
print(lambda_power2)

# 3 - solution
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(lambda x: x**x)(x) for x in myList])

# -------------------------------------------------------------------------------
circle_areas = [3.57843, 5.98032, 2.18384, 56.48219, 9.23765, 45.87365]
"""
ROUND
----------------------------------------------------------------------------
The round function is used to round floating point numbers to a desired number
of decimal places. It takes two arguments, the first one being the number to
be rounded and the second being the number of decimal places to be rounded to.
"""
round_funct_map = list(map(round, circle_areas, range(1,7))) # 1,2,3,4,5,6
print(round_funct_map)

round_funct_map = list(map(round, circle_areas, [2,2,2,2,2,2]))
print(round_funct_map)


"""
# FILTER
---------------------------------------------------------------------------------
Filter function is used to filter elements of an iterable that meets a certain
criteria. It takes two arguments, a func and an iterable
SYNTAX: filter(func, iterable)

`func` - must return a boolean
`iterable` - each element of the iterable will be passed through the func and any
    element that returns false will be removed
N/B: Unlike map, the filter function only takes one iterable
     `func` is required to return True or False.
     Each element of the iterable will be passed into the `func` and only elements
     that are True will be kept while elements that are False will be filtered
     out.
"""
chem_scores = [66, 90, 59, 76, 60, 88, 74, 81, 65]
# filter out score that are less than 60
print(list(filter(lambda x: x > 60, chem_scores)))

"""
# CLASSWORK
----------------------------------------------------------------------------
Write a program that will only return a list of chem scores that are odd numbers
using built-in functions.
"""
print(list(filter(lambda k: k % 2 != 0, chem_scores)))

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
"""
Write a program that will return a list of names that are less than or equal
to 7 letters.
"""
print(list(filter(lambda p: len(p) <= 7, my_names)))
