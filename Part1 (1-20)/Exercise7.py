# Sums all the pair intergers of a range of numbers using a loop.

def PairSum():
    print("---------------------------------------------------------------")
    print("Sums all the pair intergers of a range of numbers using a loop.")
    print("---------------------------------------------------------------")
    print()

    try:
        # Converts a string into an int and stores it in a variable
        limit = int(input("Enter the a pair number (interger) as a limit for the loop: "))

        if limit%2 == 0:  # If the limit is a pair number: 

            sum = 0
            for x in range(2, limit+1, 2):  # a +1 is added to print the use the last number from the loop.
                sum += x  # Sums all the 

            print(f"The sum from 2 to {limit} is: {sum}")   # Print the ranges an the sum.

        else:  # If the limit is not pair.
            print("Enter a pair interger.")

    except ValueError:
        print("Enter an interger.", ValueError)
