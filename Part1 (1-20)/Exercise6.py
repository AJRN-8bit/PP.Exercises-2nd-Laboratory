# Prints only the last names of a "user" list.

def LastnameSeparator():
    print("------------------------------------------")
    print("Prints only the last names of a user list.")
    print("------------------------------------------")
    print()

    try:
        # Lists with names and both last names
        list1 = ["Daniel", "Ramos", "Morales"]
        list2 = ["George", "Rodriguez", "Jimenez"]
        list3 = ["Azai", "Juarez", "Esteban"]

        full_list = [list1, list2, list3]  # Stores all the lists
        print(f"People: {full_list}")  # Prints the lists of people.

        for x in full_list:
            lastname1 = x[1]  # Stores first lastname
            lastname2 = x[2]  # Stores second lastname

            print(f"The last name is {lastname1} {lastname2}")  # Prints the both last names

    except SystemError:  # If an error occures.
        print("An error ocurred", SystemError)
