# Find the letter of an string element of a list.

color_list = ["Rojo", "Azul", "Verde", "Amarillo"]  # Initializes a color list.

def LetterFinding():
    print("------------------------------------------------")
    print("Finds the letter of an string element of a list.")
    print("------------------------------------------------")
    print()

    try:
        print("Color list: ", color_list)  # Prints the color list.
        print()

        # Prints the element "Azul" had it letter u.
        print(f"The element: {color_list[1]} has the letter {color_list[1][2]} in it") 


    except Exception:
        print("An error ocurred: ", Exception)

