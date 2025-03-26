# Checks if a fruit exists in a fruit list.

def FruitExists():
    print("--------------------------------------------------")
    print("Checks if the Cherry fruit exists in a fruit list.")
    print("--------------------------------------------------")
    print()

    try: 
        fruitList = input("Enter the fruit list (separated by spaces): ").split()  # Stores the string input like a list.

        existsCherry = "Cherry" in fruitList  # Checks if cherry is in the fruit list and stores the boolean.

        if existsCherry == True:  # If the cherry exists.
            print("Cherry exists in the fruit list.")

        else:  # If it doesnt exist.
            print("Cherry does not exists in the fruit list.")

    except ValueError: # If an error occures.
        print("Invalid input.", ValueError)
