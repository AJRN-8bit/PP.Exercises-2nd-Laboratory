# Type error exercise.

def Error2():
    print("-----------------------------------")
    print("This exercise contains a TypeError.")
    print("-----------------------------------")
    print()

    try:
        lista_colores = ["rojo", "azul" "verde", "amarillo"]
        print(lista_colores(0))
        # The index usage is with [], not with ().

    except TypeError:  # It will raise the type error.
        print("An error ocurred: ", TypeError)
