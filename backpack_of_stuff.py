import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if userChoice == "1":
        print("What item do you want to add to the backpack?")
        itemToAdd = input()

        # Adding item to backpack
        itemsInBackpack.append(itemToAdd)

    if userChoice == "2":
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()
        # Check if item is in backpack
        if itemToCheck in itemsInBackpack:
            print("Yes, " + itemToCheck + " is in the backpack.")
        elif itemToCheck not in itemsInBackpack:
            print("No, " + itemToCheck + " is not in the backpack.")
        else:
            print("Error Occurred")

    if userChoice == "3":
        sys.exit()
