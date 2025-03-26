# Shows the product table of a certain interger.

def ProducTable():
    print("----------------------------------------------")
    print("Shows the product table of a certain interger.")
    print("----------------------------------------------")
    print()

    try:
        num = int(input("Enter a number (interger): "))  # The number on which the table will be created.
        limit = int(input("Enter limit of product table (interger): "))  # Limit or size of the product table.

        i = 0  # Product result initialization.
        for x in range(1, limit +1):  # The +1 allow to use the last true value.
            i = num * x  # Calculates the result product.

            print(f"{num} x {x} = {i}")  # Prints the number, the step and the result product.

    except ValueError:
        print("Enter an interger.", ValueError)
