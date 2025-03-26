# Indentifies a user by his name and last name.

def UserIdentifier():
    print("---------------------------------------------")
    print("Indentifies a user by his name and last name.")
    print("---------------------------------------------")
    print()
    print("Try: Daniel Ramos")
    print()

    try:
        # Stores the input string in a variable.
        name = input("Enter name: ")
        last_name = input("Enter last name: ")  

        if name == "Daniel":  # If the name is Daniel it enters another if structure.
        
            if last_name == "Ramos":  # If the last name is Ramos.
                print(f"Correct name and last name: {name} {last_name}")

            else:  # If the last name is not Ramos.
                print("Incorrect last name.")

        else:  # If the name is not Daniel.
            print("Unknown user.")

    except SystemError:  # If an error occures.
        print("Error occured.", SystemError)