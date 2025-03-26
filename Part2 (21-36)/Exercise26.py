# Index error exercise.

def Error3():
    print("-----------------------------------")
    print("This exercise contains a IndexError.")
    print("-----------------------------------")
    print()

    try:
        lista_colores = ["rojo", "azul", "verde"]
        print("Element: ", lista_colores[-0])
        print("Element: ", lista_colores[-2])
        # The used indexes are out of range.

    except IndexError:  # It will raise the index error.
        print("An error ocurred: ", IndexError)
