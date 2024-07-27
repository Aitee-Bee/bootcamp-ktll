def is_palindrome(n):
    return n == n[::-1]  # reverse string and check if reverse and word are same


print(is_palindrome("civic"))


wordd = input("Enter a string: ")

if wordd == wordd[::-1]:
    print("Yeaahh")
else:
    print("Not a palindrome")
