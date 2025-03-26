# Prints a figure with an input height using a while loop.

def PrintFigure2():
    print("--------------------------------------------------------")
    print("Prints a figure with an input height using a while loop.")
    print("--------------------------------------------------------")
    print()

    try:
        # Converts the input into an int and stores it in a variable.
        num = int(input("Enter the height of the figure (try 9): ")) 

        lim = num + 1  # Adds a +1 to the input to use the last value in the loop.
        i = 0  # Empty variable initialization.
        x = 0  # Step count initialization.
        
        while (x < lim):  # This loop makes the steps of the height until the limit is reached.

            if x > int(lim/2):  # If the height is half way:
                i -= 2  # It adds a -2 value to i on every loop.

            j = 0  # Empty variable initialization.
            while (j < x + i):  # I does the loop until j is greater than the condition.
                # If i is negative, the count step (in this loop) goes backwards.
                # Prints the '*' symbol depending the step height (step 2, 2 '*' symbols), this thanks to the loop above.  
                print("*", end="")
                j += 1  # Increases the print count.

            print()  # Separates the steps by a terminal line.
            x += 1  # Step count increases on each loop.

    except Exception as e:
        print("An error ocurred: ", e)

