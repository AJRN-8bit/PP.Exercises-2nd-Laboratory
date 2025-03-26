## Prints or show all the elements inside a list using a while loop.

def SeparateElements2():
    print("-----------------------------------------------------------------")
    print("Prints or show all the elements inside a list using a while loop.")
    print("-----------------------------------------------------------------")
    print()

    try:
        list = input("Enter a string list (separated by spaces): ").split()  # Stores the strng list input into a variable.

        print()
        print("All the elements of the list:")  # Message

        x = 1  # Count initialization
        while(x < len(list) + 1): # The loop repeats itself until the lenght of the list is exceeded.
            print(f"{x}. {list[x-1]}")  # Shows the number of the element and the element itself using its index.
            x += 1  # Increases the count by one on every loop.

    except ValueError:
        print("Please enter valid elements. ", ValueError)
