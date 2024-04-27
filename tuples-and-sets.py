"""
# TUPLE
------------------------------------------------------------------
A tuple is a compound data struture in python. It is an ordered
sequence and are also immutable data struture. They care simply created
by using ().
"""
cordinates = (45673543, 8764542)
longitude = cordinates[0]
latitude = cordinates[1]
print(cordinates)
print('Longitude:', longitude)
print('Latitude:', latitude)

# cordinates[0] = 9656354

"""
# A constructor - is used to empty compound data structures
-----------------------------------------------------------------
list: list() or []
tuple: tuple() or ()
set: set()
dict: dict() or {}
"""

color = list()
colr = []
print(type(color))
print(type(colr))

# Is it possible to have a list inside a tuple?
schools = (['name', 3409, '3 years', True], ['name1', 290, '6 months', False]) # a tuple with list elements
print(type(schools))
print(schools[0])

colors = [('red', 'blue'), ('yellow', 'black')]  # list of tuples
print(type(colors))
print(colors[0])

# Because a tuple is an ordered sequence you can loop over it
for color in colors:
    print('Colors -', color)

# Functions used with tuples
cord_len = len(cordinates) # will find the length of the tuple.
print(cord_len)

cord_min = min(cordinates) # will find the smallest element of the tuple
print(cord_min)

cord_max = max(cordinates) # will find the largest element of the tuple
print(cord_max)

print(min('w', 'e', 't', 'a'))
print(max('w', 'e', 't', 'a'))

"""
# SETS
------------------------------------------------------------------
Set is a compound data structure that is unordered sequence and immutable.
A set only allows unique elements. To create an empty set, you can use a
set contructor.
"""
vowels = {'a', 'e', 'o', 'i', 'u'}
print(type(vowels))
vowls = ['a', 'a', 'e', 'i', 'i', 'o', 'u']
unique_vowels = set(vowls)
print(unique_vowels)
print(set(sorted(unique_vowels)))

for vowel in vowels:
    print('V -', vowel)

# Classwork
# Write a function that takes a list and returns only the uniques elements.



