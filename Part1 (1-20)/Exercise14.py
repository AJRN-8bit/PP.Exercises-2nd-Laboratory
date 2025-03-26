# Prints or show the repective product table from 1 to 9.

def ProductTable1to9():
    print("-------------------------------------------------------")
    print("Prints or show the repective product table from 1 to 9.")
    print("-------------------------------------------------------")
    print()

    try:
        for x in range(1, 9 +1):  # Goes from 1 to 9, each loop creates a product table for the current x value.
            p = 0  # Product result initialization.

            for y in range(1, 10 +1):  # The +1 allow to use the last true value.
                p = x * y  # Calculates the result product.
                print(f"{x} x {y} = {p}")  # Prints the number, the step and the result product.

            print()  # Separates each product table.

    except Exception:
        print("An error ocurred: ", Exception)
