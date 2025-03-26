from Exercise29 import ncolors_list as importedList  # Uses the color list from the exercise 29.
# Deletes values from an existing list. 

mcolors_list = ['Gris', 'Azul', 'Naranja', 'Rosa']  # Result list from this exercise.

def PopListElements():
    print("--------------------------------------------------")
    print("Deletes elements from the list of the exercise 29.")
    print("--------------------------------------------------")
    print()

    try:
        colors_list = importedList.copy()  # Stores the imported list.
        print("Color list:", colors_list)  # Displays the list.
        print()

        # Stores a list of indexes.
        indexes = list(map(int, input("Enter the indexes of the elements to be deleted (separeted by spaces): ").split()))
        print()

        indexes.sort(reverse=True)  # Enalbles the index to not move during elimination.

        for x in indexes:  # Deletes every element using the index list.
            colors_list.pop(x)

        print("Modifed color list: ", colors_list)  # Displays the modified list.


    except IndexError:
        print("An error ocurred: ", IndexError)

