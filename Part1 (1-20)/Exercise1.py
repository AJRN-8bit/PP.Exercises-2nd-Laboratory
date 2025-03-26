# Checks if an entered age is on the legal age range and prints a message.

def CheckAge():
    print("------------------------------------------------------------------------")
    print("Checks if an entered age is on the legal age range and prints a message.")
    print("------------------------------------------------------------------------")
    print()

    try:
        age = int(input("Enter age (interger): "))  # It converts the string into an int and stores it in a variable.

        if age >= 18:  # Checks if the age is greater or equal than 18.
            print("You are in the legal age.")

        else:  # It executes if the age is less than 18.
            print("You are not in the legal age.")

    except ValueError:  # If an error occures.
        print("Please enter a valid interger", ValueError)


        