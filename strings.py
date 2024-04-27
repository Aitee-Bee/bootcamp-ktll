"""
# STRINGS
-------------------------------------------------------
A string is simply a sequence of characters enclosed 
either in single quote '' or double quote "".

A string could be just about any alpha-numeric character
"""
# Examples
"I am learning Python." # string with a double quote
'I am learning Python.' # string with a single quote

# When creating a string you have to be consistent with the opening and closing quote
# What is the difference between single and double quote
# There is no difference except for a specail case of the examples below
'I\'m a hungry' # you can escape the inner single quote by typing \ before it
"I'm a hungry"
"I\"m a hungry"
'I\"m a hungry'

# We can concatenate (join) two string
first_name = "Itoro"
last_name = "Uduak"
full_name = first_name + " " + last_name
print("Itoro" + "Uduak")
print(full_name)

# You can also multiply a string with an integer
hail_itoro_2x = "Itoro " * 4
print(hail_itoro_2x)

# We can find the length of a string
print(len("Itoro"))
print(len("Itoro "))


# STRING FORMATTING
print("Itoro".upper())
print("Itoro".lower())

print("My name is " + first_name)
print("My name is " + first_name + ' ' + last_name)
print('My name is', first_name, last_name)
print('My name is {} {}, my fullname is {}'.format(first_name, last_name, full_name)) # {} is called a placeholder. This is using format function
# The first placeholder will be replaced by the first value of format() 
# and the second placeholder will be replaced by the second value of format()
print(f'My name is {first_name} {last_name}') # this is called the f-string method of formatting strings

"""
# 03 March 2024 - Strings
----------------------------------------------
"""

# Accessing the elements of a string
"""
# String indexing
----------------------------------------------
- String indexing has to do with accessing the individual letters that 
makes up a string using their corresponding indexes

- In python index starts from zero. That means that the first letter
of a string has index number zero (0).
- The index must be an integer. You cannot use a float as an index, Python
will throw and error called TypeError
- You can also use negative integers as index.
"""
sentence = 'A quick brown fox'
word = 'python'

# We can retrieve the first letter from the variables
print(sentence[0]) # this will give us the first letter in sentence
print(word[1]) # this will give us the second letter in word
print(sentence[-1]) # this will give us the last letter

"""
# classwork
-------------------------------------------------------
Create a variable called fruits and assign your best fruit to it, then
retrieve the third letter of the fruit
"""
# Classwork solution
fruits = 'banana'
print(fruits[2])

"""
# String Slicing
--------------------------------------------------------
- String slicing has to do with using indexes to retrieve part of the letters
of a string.
- In string slicing, you will need three values
    - start: index where you want to start extracting from
    - stop: index where you want to stop + 1
    - step: how many letters should be counted in succession
- When you are doing string slicing, the last number should be 1 higher than
index of where you want to stop.
"""
statement = 'Python is a very interesting programming language'

# Extract only the word 'Python' from statement
print(statement[0:6]) # this has a step of 1
print(statement[0:6:2]) # this has a step of 2
print(statement[-8:]) # when you leave out the stop value, python takes it to mean till the end
print(statement[:6]) # when you leave out the start value, python takes it to mean from the beginning
print(statement[:]) # when you leave out both start and stop, it will give you a copy of the original string
print(statement[-8:-4])
print(statement[:8])

"""
# 11 March 2024
"""
# Revision
language = 'Python'
color = 'Blue'
phrase = 'i are hungry'

# Question: write a command that will give this output 'hun' using the phrase
print(phrase[6:9])

# classwork for Mayen
# Write a command that will give 'are' using the variable phrase
print(phrase[2:5])

"""
# TOPIC: Checking if a substring is available in a string
To check if a substring is in a string we use `in`
"""
color = 'Purple'
# I want to check if purple has letter 'r' `in` it
print('r' in color) # the result of this is a boolean or bool
print('i' in color)

# Imagine that you ask someone for a string, then you want to check if a
# certain substring is in that string that the person typed

# Checking for the length of a string
# To check for the length of a string use the function called `len()`
length_of_color = len(color) # the result of this is a integer
print(length_of_color)

# Checking the index of a letter in a string
word = 'information'
# to find the index of a letter you use the function `index`
print(word.index('i'))

