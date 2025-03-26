from Exercise27 import color_list as importedList  # Uses the color list from the exercise 27.
# Adds values from an existing list.

ncolors_list = ['Gris', 'Rojo', 'Azul', 'Naranja', 'Verde', 'Amarillo', 'Rosa'] # Result list from this exercise.

def AddListElements():
    print("----------------------------------------------")
    print("Add elements to the list from the exercise 27.")
    print("----------------------------------------------")
    print()

    try:
        colors_list = importedList.copy()  # Stores the imported list.
        print("Color list: ", colors_list)
        print()
        
        # Stores a list of colors
        colors_toadd = input("Enter a list fo color to add (only three) (separated by spaces): ").split()
        print()

        indexList = [0, 5, 3]  # Position of the color to be inserted.

        for color, index in zip(colors_toadd, indexList):  # Ii adds the colors using the indexes and to add lists.
             colors_list.insert(index, color)

        print("Modified color list: ", colors_list)  # Displays the modified color list.

    except IndexError:
        print("An error ocurred:", IndexError)
