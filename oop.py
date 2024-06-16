"""
Create a tuple of 6 email adresses, then write a function
that takes the tuple as argument. The function will check if the
email is not ending with a ".com", it will change it to a ".com"
and add it to a list. If it is ending with a ".com", it will
simply just add it to the list. Then will return the list.

'wilson@gmail.net', 'swedishgee@yahoo.com', 'pelstop@gmail.com', 'deniah@gmail.edu'
"""
"""
# Object Oriented Programming OOP
-------------------------------------------------------------------
Object oriented programming is a programming concept that provides a
means of structuring your program in such a way that it can be referred to
as objects, with properties and behaviours.

Properties can also be reffered to as attributes.
Behaviours can also be thought of as abilities to do something.

Take some analogy from a car. A car can be seen as an object.
A car as an object has properties and can be said to have behavious.
Properties of a car can include color, model, number of doors, manufacturing year.
Behaviours of a car can include moving, uses fuel, fume.

Back to OOP
Here we see our program as basically an object which is an instance of a class,
that has properties and behaviours.
We represent these properties with variables inside the class while we represent
the behaviours using methods in the class. A method is simply a function that is
inside a class.

To write a class in Python, we use the keyword "class" followed by the name of the
class written in camel case of this form, "Car" or "BenzCar".

"""
# Example of a class with one word
class Car:
    pass

# Example of a class with more than one word
class BenzCar:
    pass

class ToyotaCar:
    pass

# Example of a class with properties
class Car:
    color = "red"
    doors = 4

# Example of a class with properties and behaviours
class Car:
    _color = "red"
    _doors = 2

    def _move():
        return "a car can move by driving"
    
    def fume():
        return "a car can fume while driving"
    
    def reverse():
        return "a car can go backwards"

car1 = Car() # this is how to create a car object by creating an instance of a car class
car2 = Car()
car3 = Car()

car1.color # this will give me the color of car1 object
car2.doors # this will give me the color of car2 object




"""
For programs that are written using classes, we say that an object
is the INSTANCE of a class.
"""

"""
# Goals of OOP
---------------------------------------------------------
* Robustness - as a software developer, you want to write programs
that produces the same right output for all anticipated inputs.
* Adaptability - you want to write programs that can evolve, responding
to changes from the environment.
* Reusablity - the same code should be able to be used in other
software components.
"""

"""
# Principles of OOP design
--------------------------------------------------------------
* Modularity - refers to an organizing principle in which different
components of a software system are divided into seperate functional units.
* Abstraction - a notion to breakdown a complicated system down to
its fundamental parts.
Abstraction is providing a generalization (say, over a set of behaviours)
* Encapsulation - is hiding the implementation details.
This entails that you write your program in such a way that
it does not reveal the internal details of how they are implemented.
Python was not created to naturally implement encapsulation like some
other programming languages. So, by convention, names of variables or
methods that starts with a single underscore character (e.g _check_balance)
are asummed to be nonpublic.
"""


"""
Class constructor
------------------------------------------------------------------
This is primarilily responsible for establishing the state of a 
newly created object. It will take care of assigning the right
values to the class attributes/properties. 

Remember that we use variables to define these attributes, thus
when we define these variables diriectly inside the class and
not inside the class constructor, they are called class attributes.
But if we define them inside the constructor, they are called
instance attributes.

SELF INDENTIFIER
------------------------------------------------------------------
The self identifier basically identifies the instance upon which a
method is invoked/called.
"""
class CreditCard:
    chip = True # class attributes

    def __init__(self, cvv, expring_date):
        self.cvv = cvv # instance attributes
        self.expring_date = expring_date # instance attributes
