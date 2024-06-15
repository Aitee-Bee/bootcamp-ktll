fifth_power = lambda a: a ** 5
print(fifth_power(2))


numbers = [48, 16, 37, 4, 12, 2]
square = list(map(lambda x: x ** 2, numbers))
print(square)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [(lambda x: x ** x)(x) for x in myList]
print(result)


chem_scores = [28, 29, 30, 31, 32, 33, 34, 35, 36]
print(list(filter(lambda x: x % 2 != 0, chem_scores)))


my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda x: len(x) <= 7, my_names)))


