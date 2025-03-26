# Prints a figure with an input height using a for loop.

def PrintFigure1():
    print("------------------------------------------------------")
    print("Prints a figure with an input height using a for loop.")
    print("------------------------------------------------------")
    print()

    try:
        # Converts the input into an int and stores it in a variable.
        num = int(input("Enter the height of the figure (try 9): ")) 

        lim = num + 1  # Adds a +1 to the input to use the last value in the loop.
        i = 0  # Empty variable initialization.
        
        for x in range(0, lim):  # This loop makes the steps of the height.

            if x > int(lim/2):  # If the height is half way:
                i -= 2  # It adds a -2 value to i on every loop.

            for _ in range(0, x + i):  # If i is negative, the count step (in this loop) goes backwards.
                # Prints the '*' symbol depending the step height (step 2, 2 '*' symbols), this thanks to the loop above.  
                print("*", end="")  

            print()  # Separates the steps by a terminal line.

    except Exception as e:
        print("An error ocurred: ", e)
