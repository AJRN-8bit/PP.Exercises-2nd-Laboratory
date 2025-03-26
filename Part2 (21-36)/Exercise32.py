# Checks how many values are repeated in a list.

num_list = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

def RepeatedValues():
    print("----------------------------------------------")
    print("Checks how many values are repeated in a list.")
    print("----------------------------------------------")
    print()

    try:
        print("List of numbers: ", num_list)  # Displays the number list.
        print()

        repeatedTimes = 0  # Variable initialization.

        for x in num_list:  # For every element in the list, if its equal to ten, the counter goes up.
            if x == 10:
                repeatedTimes += 1  

        print(f"The value 10 is repeated {repeatedTimes} times.")  # Displays how many times the numbers is repeated.


    except Exception:
        print("An error ocurred: ", Exception)

