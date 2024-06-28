shopping_list = []
print("Welcome Itoro's shopping mall")
while True:
    choice = input(
        "Enter 0-to-exit; 1-to add item; 2-to remove item; 3-to view items in your cart "
    )

    if int(choice) == 0:
    choice = int(input("Enter 0-to-exit; 1-to add item; 2-to remove item; 3-to view items in your cart "))
    
    if choice == 0:
        break

    if choice == 1:
        print("You can only add 5 items.")
        for i in range(1, 6):
        cart = {}
        for i in range(1,6):
            item = input("Enter an item: ")
            cart[f"item{i}"] = item
            print(f"You have {i} item in the cart")
        print(f"Here are the items in your cart {shopping_list}")
        checkout = int(input("Do you want to checkout now? Press 5"))
    elif int(choice) == 2:
        shopping_list.append(cart)
        
        print(f"Here are the items in your cart: {shopping_list}")
        # checkout = int(input("Do you want to checkout now? Press 5"))

    elif choice == 2:
        print(f"Items in your cart: {shopping_list}")
        del_choice = input("Enter 0 to empty the cart or an item you want to remove: ")
        if del_choice in shopping_list:
            shopping_list.remove(del_choice)
            print(f"{del_choice} has been removed successfully.")
            print(f"Items left in cart: - {shopping_list}")
        elif int(del_choice) == 0:
            shopping_list.clear()
            print("Your cart is empty.")
    elif choice == 3:
        for item in shopping_list:
            print(item)


"""
DRY - Don't Repeat Yourself
"""

cart = [
    {
        "item_one": "spoon",
        "item_two": "yoghurt",
        "item_three": "towels",
        "item_four": "biscuit",
        "item_five": "juice",
    }
]
