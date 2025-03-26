from Exercise32 import num_list  # Imports the number list from the exercise 32

# Sorts the number list to start from smallest to greatest.

def Sort_StoL():
    print("------------------------------------------------------------------------------")
    print("Sorts the number list from the exercise 32 to start from smallest to greatest.")
    print("------------------------------------------------------------------------------")
    print()

    try:
        print("Number list: ", num_list)  # Prints the number list.
        print()

        # Creates a new list, its the sorted number list, but in ascending order.
        orderList = sorted(num_list, reverse= False)  

        print("Number list in ascending order: ", orderList)

    except Exception as e: print("An error ocurred: ", e)