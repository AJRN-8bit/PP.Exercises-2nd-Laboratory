# Name error exercise.

def Error1():
    print("-----------------------------------")
    print("This exercise contains a NameError.")
    print("-----------------------------------")
    print()

    try:
        lista_colores ["rojo", "azul", "verde", "amarillo"]
        # The line above is missing the "=" symbol for defining.

    except NameError:  # It will raise the name error.
        print("An error ocurred: ", NameError)
