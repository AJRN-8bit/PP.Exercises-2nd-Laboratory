from Exercise21 import num_list as importedList  # List importation
# Prints a specific element from a list using its index.

def ListUsage2():
    print("--------------------------------------------------")
    print("Shows an element from the exercise 21 number list.")
    print("--------------------------------------------------")
    print()

    
    try:
        num_list = importedList  # Storing the imported list in a variable.
 
        # Prints the element 76 of the list using its index.
        print(f"Element of the number list: {num_list[3]}")

    except:
        print("An error ocurred.")
