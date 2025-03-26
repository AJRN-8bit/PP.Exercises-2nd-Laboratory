from Exercise30 import mcolors_list as importedList  # Uses the color list from the exercise 30.
# Copies an existing list

def CreateListCopy():
    print("-------------------------------------")
    print("Copies the list from the exercise 30.")
    print("-------------------------------------")
    print()

    try:
        colors_list = importedList  # Stores the imported list.
        copy_list = colors_list.copy()  # Makes a copy of that list.
        print(copy_list)  # Displays the copy list.

    except:
        print("An error ocurred.")

