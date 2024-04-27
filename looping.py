"""
# LOOPING IN PYTHON
--------------------------------------------------------
# in python a loop is simply what repeats itself

There are two types of looping in Python
- while loop
- for loop

WHILE LOOP
---------------------------------------------------------
The while loop is used when you do not know the exact number
of times you want the loop to run.
So it means that a while loop is sutibale when you want to keep
running the loop till a certian condition is met.
The while loop only needs a condition that will be tested each
time the loop runs


FOR LOOP
----------------------------------------------------------
The for loop is used when you know the exact number of times
you want the loop to run.
So it means the for loop is suitable when you have an exact
number of times before hand you want the loop to run.

Usually, the for loop is used with the range() function. The
range() function generates a list of numbers within a start
value and an end-1 value

range function takes 3 argument
- start value
- end value
- step value
range(start, end, step) - this will give you values from start to end-1 with step
range(end) - this will give you from 0 to end-1, and assume the step to be 1
range(start, end) - this will give you values from start to end, and assume the step to be 1

"""
# Example - while loop
# when you are doing while loop you MUST set a value outside the loop
counter = 1
while counter < 7:  # the condition that must always be True
    print("I are hungry.", counter)
    counter = counter + 1  # you must increase or decrease this inside the loop, or else your loop will run infinitly


age = 30
while age > 23:
    print("You can work for us", age)
    age = age - 1  # decrease the value of age
    
cups = 0
while cups <= 5:
    print('Add more cups', cups)
    cups = cups + 1

# 25 March 2024 - continuation of loops
# Revision
current_age = 25
employement_age = 25
retirement_age = 70
promote_after = 4
while current_age < retirement_age:  # looping is used because it will be a repeated thing
    # check if current is the same with employment age we will continue
    if current_age <= employement_age:
        current_age = current_age + promote_after
        continue # means do not proceed with the other lines in the loop, instead go and start from the begining again
    # continue to promote the person after every 4 years
    print("You have been promoted.", current_age)
    current_age = current_age + promote_after
print("You are a retireeeee now")

# Classwork
"""
Write a while loop that prints only even numbers between 1 and 20. Tip: use the modulo operator
"""
# solution is done down down


# For loop
""""
The for loop works with only things that are iterable.
Iterable means it can pick one item at a time.

So data types/strutures that are iterable in python include
- strings
- list
- dictionary
"""
for letter in "python":
    print(letter)
print("---------------------------------------------")
for number in range(1,10):  # range(1,10) will give you a sequence of numbers 1,2,3,4,5,6,7,8,9
    print(number)
print("---------------------------------------------")
for number in range(10):    # range(10) will give a sequence of numbers 0,1,2,3,4,5,6,7,8,9
    print(number)
for i in range(21):
    if i % 2 == 0:
        print(i)
        
# 31-03-2024
"""
A for loop is used when we know before hand how long we want the loop to run.
"""
# Example: If I want to loop for 10 times
for number in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print("Time - ", number)

print("---------------------------------------------------")

for number in range(1, 11): # 1 is the start value and 11 - 1 will be the stop value: 1,2,3,4,5,6,7,8,9,10
    print("Time - ", number)

print("---------------------------------------------------")

# Only even numbers between 0 and 20
for i in range(0, 20, 2): # the last value is the step value, so it will count by 2 numbers:
    if i == 0:
        continue # this means jump to the next loop
    print("Even number - ", i)

for x in range(0, 20, 2):
    if x == 16:
        break # this means stop the loop, don't go any futher, don't loop again
    print("Even numbers up to 16 - ", x)

# something interesting
word = 'programming'
vowels = ['a', 'e', 'i', 'o', 'u'] # is a `list` of letters. A list is written with []

for letter in word:
    # check if the letter is in vowels
    if letter in vowels:
        print("I am a vowels,", letter)

value = 2
for x in range(1, 25):
    # print("Value raised to the power of x is", value**x) # just the usual way
    # print(f"Value raised to the power of x is {value**x}") # this is called the f-string pattern
    print("Value raised to the power of x is {}".format(value**x)) # using the format method

for x in range(1, 25):
    print(value, "raised to the power of", x ,"is", value**x) # just the usual way
    # print(f"{value} raised to the power of {x} is {value**x}") # this is called the f-string pattern
    # print("{} raised to the power of {} is {}".format(value, x, value**x)) # using the format method


# solution for a classwork up up
counter = 1
while counter < 20:
    if counter % 2 == 0:
        print(counter)
    counter += 1
    
# More examples on WHILE loop
"""Ask a user for a value and the user's favourite word, then cheer the word by the number of times given."""
fav_number = int(input("What is your favourite number? ")) # input function always collect string values, so we can type cast it to integer
fav_word = input("What is your favourite word? ")
counter = 0
while counter < fav_number:
    print(fav_word)
    counter += 1

