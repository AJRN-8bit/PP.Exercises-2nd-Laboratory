# Stops showing the list elements if a specific element is met.

def ShowElementsUntil1():
    print("-------------------------------------------------------------")
    print("Stops showing the list elements if a specific element is met.")
    print("-------------------------------------------------------------")
    print()

    try:
        trees = ["Manzano", "Pino", "Madroño", "Eucalipto", "Nogal", "Olivo", "Almendro"]  # List of trees.
        print("Trees:", trees)  # Shows the list tree.

        for tree in trees:  # Prints every tree in the list of trees.
            print(tree) 

            if tree == "Nogal":  # If a specific tree is met, it breaks the loop.
                break

    except Exception:
        print("An error ocurred: ", Exception)

