# Prints or show all the elements inside a list using a for loop.

def SeparateElements1():
    print("---------------------------------------------------------------")
    print("Prints or show all the elements inside a list using a for loop.")
    print("---------------------------------------------------------------")
    print()

    try:
        list = input("Enter a string list (separated by spaces): ").split()  # Stores the strng list input into a variable.

        print()
        print("All the elements of the list:")  # Message

        x = 1  # Count initialization
        for elem in list:  # The loop repeats itself for every existing element in the list.
            print(f"{x}. {elem}")  # Shows the number of the element and the element itself.
            x += 1  # Increases the count by one on every loop.

    except ValueError:
        print("Please enter valid elements. ", ValueError)
