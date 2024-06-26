shopping_list = []
print("Welcome Itoro's shopping mall")
while True:
    choice = input("Enter 0-to-exit; 1-to add item; 2-to remove item; 3-to view items in your cart ")
    
    if int(choice) == 0:
        break

    if int(choice) == 1:
        print("You can only add 5 items.")
        for i in range(1,6):
            item = input("Enter an item: ")
            shopping_list.append(item)
            print(f"You have {i} item in the cart")
    elif int(choice) == 2:
        print(f"Items in your cart: {shopping_list}")
        del_choice = input("Enter 0 to empty the cart or an item you want to remove: ")
        if del_choice in shopping_list:
            shopping_list.remove(del_choice)
            print(f"{del_choice} has been removed successfully.")
            print(f"Items left in cart: - {shopping_list}")
        elif int(del_choice) == 0:
            shopping_list.clear()
            print("Your cart is empty.")
    elif int(choice) == 3:
        for item in shopping_list:
            print(item)


