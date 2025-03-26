from Exercise21 import num_list as importedList  # List importation 
# # Prints the smallest and greatest vales inside an interger list. 


def ListUsage3():
    print("------------------------------------------------------------------------")
    print("Shows the maximum and the minimum values of the exercise 21 number list.")
    print("------------------------------------------------------------------------")
    print()

    try:
        # Usage of the list from the exercise 21
        num_list = importedList 

        # Prints the smallest and greatest vales inside the list.
        print(f"Smallest value in the list: {min(num_list)}.")
        print(f"Greatest value in the list: {max(num_list)}.")

    except:
        print("An error ocurred.")