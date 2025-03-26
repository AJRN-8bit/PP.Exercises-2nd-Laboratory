# Stops showing the list elements if a specific element is met, and prints a message if its not found.

def ShowElementsUntil2():
    print("----------------------------------------------------------------------------------------------------")
    print("Stops showing the list elements if a specific element is met, and prints a message if its not found.")
    print("----------------------------------------------------------------------------------------------------")
    print()

    try:
        trees = ["Manzano", "Pino", "Madroño", "Eucalipto", "Nogal", "Olivo", "Almendro"]  # List of trees.
        print("Trees:", trees)  # Shows the list tree.

        inputTree = input("Enter the name of a tree: ")

        found = False  # Boolean initialization.
        for tree in trees:  # Prints every tree in the list of trees.
            print(tree) 

            if tree == inputTree:  # If a specific tree is met, it breaks the loop.
                found = True  # If the tree is found changes the boolean to true.
                break

        if found == False:  # If the tree is not found
            print(f"{inputTree} tree not found.")
        
        
    except Exception:
        print("An error ocurred: ", Exception)
