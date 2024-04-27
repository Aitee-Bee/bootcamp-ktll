# Boolean and Conditional Logic

# Boolean: a bool is a data type in Python that is
# either `True` or `False`

"""
# Conditional Logic
--------------------------------------------------------------
In Python, we can logical test the condition of something
and the make some certain decisions based on the result of
the test we did.

How can we write a logial test statement?
-----------------------------------------
We can use mathematical operator or logical operators to write a 
test statement. The result of a test statement is always a bool.

Which mathematical operators can we use to write a test statement?
# Mathematical Operators
---------------------------------
< less than
> greater than
<= less than or equal to
>= greater than or equal to
== equal to

What are the logical operators?
Logical Operators
----------------------------------
and : gives a True only when both sides are True

True and True == True
True and False == False
False and True == False
False and False == False
--------------------------------------------------------------------
or :  gives a False only when both sides are False

False or False == False
True or False == True
False or True == True
True or True == True
--------------------------------------------------------------------

You can read up `Truth Table` on line

--------------------------------------------------------------------
A logical statement is going to be an expression with something on
the left and something on the right with the operator in between them
"""
print(4 < 7) # 4 < 7 is a logical statement or expression
print(6 == 1)
print(7 <= 7)

print(4 > 4 and 3 == 1) # bool and bool -> False and False == False
print(3 < 2 or 2 < 2) # bool or bool -> False or False == False

"""
# Branching statement using `if statement`
--------------------------------------------------------------------
The branching statement is done in Python using the if function.

It allows you perform certain opertations or task based on the result
of a logical statement.

The if statement must evaluate to True

You can have a single or multiple if statements.

A single if statement has one conditional statement
A multiple if statement has two or more conditional statement

N/B: the else statement does not have a conditional statement
"""
# Examples for a single if statement
if 4 == 1: # the logical statement here is evaluated base on Truth value
    print('We are winners') # this will only run on the condition that the logical statement was True

if 3 < 7:
    print('This is now going to be printed')
    
# In a case where we want to still do something when it evaluated to False
if 4 == 1: # this evaluates to False
    print('This will not print in this situation') # this will not print
else: # you need to have this else statement to cover for the situation where the logical statement was False
    print('This is what will be printed') # this is what will be printed

# Example for a multiple if statement
if 4 > 5:
    print('Yes we are going higher')
elif 4 < 5:
    print('It was actually the other way round oh!!!')
elif 5 == 5:
    print('We are even')
else:
    print('Omo we have lost our way oh!!!')
    
# Revision
"""
How do we use the elif?
How does the modulo work?
"""

# elif
# How to ask a user for a value (int) or string
# We can ask a user to type something for us using?
color = input("What is your name? ")
print(color)

# elif allows you write multiple ifs which enables you to test for more conditions
if color == 'Yellow':
    print("I have been expecting you", color)
elif color == 'Blue':
    print("Where have you been", color, "my friend")
elif color == "Red":
    print("You have been so far away", color)
else:
    print("I have no colors left")

# modulo - this is used to find the remainder of a division
print("division", 4/2)

# elif
# How to ask a user for a value (int) or string
# We can ask a user to type something for us using?
color = ''

# elif allows you write multiple ifs which enables you to test for more conditions
if color == 'Yellow':
    print("I have been expecting you", color)
elif color == 'Blue':
    print("Where have you been", color, "my friend")
elif color == "Red":
    print("You have been so far away", color)
else:
    print("I have no colors left")

# modulo - this is used to find the remainder of a division
print("division", 4/2)
print("division", 5/2)
print('remainder using modulo', 4%2)
print('remainder', 5%2)

# syntax error only comes when you don't type correctly in python
if 1 < 8:
    print("Yes it is")
