from random import uniform

shopping_list = []

print("Welcome to Itoro's Shopping Mall")

while True:
    choice = int(input("Enter \n 0-to-exit; \n 1-to add item; \n 2-to remove item; \n 3-to view items in your cart \n "))
    
    if choice == 0:
        break

    if choice == 1:
        print("You can only add 5 items")
        cart = {}
        for i in range(1,6):
            item = input("Enter an item: ")
            cart[f"item{i}"] = [item, round(uniform(77.5, 240.9), 2)]
            print(f"You have {i} item in the cart")
            for key, value in cart.items():
                print(f"'{key}: {value}'")
        shopping_list.append(cart)
        
        # print(f"Here are the items in your cart: {shopping_list}")
        checkout = int(input("Press 0 to checkout cart; \n Press 1 to remove an item "))
        if checkout == 0:
            # do something here
            pass
        elif checkout == 1:
            pass

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

