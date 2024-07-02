shopping_list = []

print("Welcome to Itoro's Shopping Mall")

while True:
    choice = int(
        input(
            "Enter 0- to exit; 1-to add an item; 2- to remove an item; 3- to view cart "
        )
    )

    if choice == 0:
        break

    if choice == 1:
        print("You can only add 5 items")
        cart = {}
        for i in range(1, 6):
            item = input("Enter an item ")
            cart[f"item{i}"] = item
            print(f"You have {i} item in the cart")
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
