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

# car1.color # this will give me the color of car1 object
# car2.doors # this will give me the color of car2 object




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
This is primarily responsible for establishing the state of a 
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
class CreditCardOld:
    instance_count = 0 # class attribute

    def __init__(self, name, cvv, expring_date): # constructor
        self.name = name # instance attribute
        self.cvv = cvv # instance attribute
        self.expring_date = expring_date # instance attribute

    def get_name(self): # a function associated with a class is called a method
        return self.name


# instantiate the CreditCard class
itoro_credit_card = CreditCardOld("itoro", 438, "15/28")
itoro_credit_card.instance_count += 1


uduak_credit_card = CreditCardOld("uduak", 934, "21/29")
uduak_credit_card.instance_count += 5

def greeting(name):
    return 'hello' + name

greeting('mfon')


"""
Docstring
Is a paragraph the tells a user how to use the class or
method or even ordinary function.
"""

class CreditCard:
    """A simple credit card."""
    number_of_instance = 0 # class attribute

    def __init__(self, customer_name, bank, card_type, account):
        """Instantiate the class with new attributes.
        
        customer_name: the name of the card holder
        bank: the issuer bank name
        type: the type of the card. e.g master, verve, visa
        account: the account number associated with card
        balance: the initial balance of the card
        """
        self.customer_name = customer_name
        self.bank = bank
        self.card_type = card_type
        self.account = account
        self.limit = 100
        self.balance = 0
        self.instance = 0
        CreditCard.number_of_instance += 1
        self.set_instance()
    
    def get_customer_name(self):
        """Return the name of the card holder."""
        return f"customer's name: {self.customer_name}"

    def get_bank(self):
        """Return the name of the bank."""
        return f"bank name: {self.bank}"
    
    def get_balance(self):
        """Return the balance."""
        return self.balance
    
    def set_balance(self, balance):
        """Set the value for balance."""
        self.balance = balance
    
    def set_instance(self):
        """A trial example."""
        self.instance += 1

    def charge(self, amount):
        """Debit the card a given amount, 
        assuming there is sufficient balance.
        
        Return True if the transaction was successful, False otherwise.
        """
        if self.balance > amount:
            return True
        else:
            return False

    def make_payment(self, amount):
        """Process a payment made with the card."""
        if self.balance < amount + self.limit:
            return "Insufficient funds."
        else:
            self.balance -= amount


uduak_card = CreditCard("Uduak", "keystone", "master card", 6758473893)
itoro_card = CreditCard("Itoro", "access", "master card", 558693875)
emem_card = CreditCard("Emem", "zenith", "verve", 8768574637)

print(uduak_card.set_balance(19000))
print(uduak_card.get_balance())
print(uduak_card.number_of_instance)
print(uduak_card.instance)

print(itoro_card.number_of_instance)
print(itoro_card.instance)
print(emem_card.number_of_instance)
print(emem_card.instance)

"""
# INHERITANCE
---------------------------------------------------------------------
Inheritance is the process by which a class takes all the attributes
and methods from another class.

Here we are looking at a parent, child relationship.
In python, a class inherits from another that is passed into it as
an argument.
"""
class Parent:
    name = "parent"

    def height(self):
        return 4.5

class Child(Parent):
    name = "child"

    def height(self):
        return 6.2

parent = Parent()
print(parent.name)
print(parent.height())
child = Child()
print(child.name)
print(child.height())

class Rectangle:
    """The parent class."""

    def __init__(self, width=0, height=0):
        """Initialize the class and set the value for width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width property."""
        return self.width
    
    @property
    def height(self):
        """Get the height property."""
        return self.height

    @width.setter
    def width(self, value):
        """ Set the value of the width attribute."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be greater than 0')
        self.width = value

    @height.setter
    def height(self, value):
        """Set the value of the height attribute."""
        if isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.height = value

    def area(self):
        """Calculate the area of a square."""
        return (self.height * self.width)
        
class Square(Rectangle):
    """A square class."""
    
    def area(self):
        """Calculate the area of a rectangle."""
        return (self.height * self.height)



