# def print_full_name(first_name, last_name):
#     print(first_name + last_name)


# first_name = "itoro"
# last_name = "etimfon"
# my_full_name = first_name + last_name
# print_full_name(first_name, last_name)


# def asking_username():
#     print("What's your name? ")
#     username = input()
#     return username


# decrement_list = [1, 2, 3, 4, 5, 6]
# decr = list(map(lambda i: i - 1, decrement_list))
# print(decr)


# users = [{"username": "Samu", "tweets": ["I love cake", "I love flour"]},
#          {"username": "Katy", "tweets": ["I love my cat"]},
#          {"username": "Bob123", "tweets": []},
#          {"username": "Guitar_girl", "tweets": []}
#          ]

# inactives = list(filter(lambda u: u["tweets"], users))
# print(inactives)


# remove_negatives = [0, -1, 2, -3, 4, -5, 6, -7, -8, 9, -10]

# result = list(filter(lambda n: n >= 0, remove_negatives))
# print(result)

# vowels = ['a', 'e', 'i', 'o', 'u']


# def findings(vowels, *args):
#     vowels = []
#     for word in args:  #for every letter in the word
#         if word[0] in vowels:
#             vowels.append(word)
#     return word
    
    
# print(findings(vowels, "bananas", "apples"))

# #vowels = "aeiou"

# create a list of names of 8 books. then create another list that only holds the books that have names shorter than 8

books = ['Ephesians', 'Genesis', 'Mark', 'Acts', 'Zephaniah', 'Exodus', 'Leviticus', 'John']

n_books = []

for book in books:
    if len(book) < 8:
        n_books.append(book)
print(n_books)


