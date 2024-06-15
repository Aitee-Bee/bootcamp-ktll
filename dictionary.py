"""
DICTIONARY
------------------------------------------------------------
A dictionary is a compund data structure that is defined by
key-value pairs.
A dictionary can have the other data types and compound data
structures that we have considered so far.
To define a dictionary you use the {} or the dict() constructor.
Dictionary are mutable data structures.
A dictionary can be used to organize data in collections

KEYS:
- Every key of a dictionary must be of immutable type eg. strings, integers, tuples, booleans
- Every key of a dictionary must be unique

VALUES:
- You can use almost any data type/structure for the values eg, list, strings, integers, tuples, dictionary

You can access the values of a dictionary using the keys
"""
students = {}  # this defines an empty dictionary
students = {'name': 'Peter', 'gender': 'male', 'age': 56}
js1_students = {'A': {'teacher': "Lawrence", 
                      'stud_count': 45, 
                      'names': ['brown', 'luke', 'william'], 
                      'stud_emails': ('brown@email.com', 'luke@email.com', 'william@email.com')
                      }
                }

# Accessing the values of a dictionary by using the keys
stud_name = students['name']
stud_age = students['age']
print(js1_students['A']['stud_emails'][0])

print(stud_name)
print(stud_age)

colors = ['red', 'blue', 'black']
colors[0]

print('------------------values------------------------')  
for stu in students:
    print(students[stu])

print('------------------keys--------------------------')  
for stu in students:
    print(stu)

"""
# CLASSWORK
-----------------------------------------------------------------------------------
Create a dictionary of at least 3 flowers with at least 2 features of each flower
and each of their botanical names.
"""
flowers = {
    'hibis': {
        'features': [],
        'botanical_name': 'poloranko'
    },
    'queen-of-the-nnight': {
        'features': [],
        'botanical_name': 'poloranko'
    },
    'wilson': {
        'features': [],
        'botanical_name': 'poloranko'
    },
    'sibmi': {}
}

print(flowers['hibis']['botanical_name'])


# checking for a key in dictionary
if 'sibmi' in flowers:
    print(flowers['sibmi'])
else:
    flowers['sibmi'] = {}  # add a new key with an empty dictionary

# print(flowers)

"""
CLASSWORK
---------------------------------------------------------------------
Create a dictionary of account details of customers of a bank. You can
use the different customer account number as keys and each account number
may have up to 3 properties.
"""

