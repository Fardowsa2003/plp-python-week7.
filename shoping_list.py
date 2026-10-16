
shopping_list = []

print("Welcome to the Shopping List Manager!")

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "added to the list.")
        else:
            print("Please enter an item.")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from the list.")
        else:
            print(item, "is not in the list.")

    elif choice == "3":
        print("\nYour Shopping List:")

        if shopping_list:
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-4.")
