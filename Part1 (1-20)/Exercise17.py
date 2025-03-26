# Stores the pair numbers of any list of interger numbers.

def PairNumberSaver():
    print("--------------------------------------------------------")
    print("Stores the pair numbers of any list of interger numbers.")
    print("--------------------------------------------------------")
    print()

    try:
        # Saves the input of a list of numbers in a list variable.
        numList = list(map(int, input("Enter numbers (intergers) (separated by spaces): ").split()))

        # Using a for loop, it selects the numbers of the numList that are pair and stores them in a new list.
        pairList = [x for x in numList if x % 2 == 0]  
        print("Pair list: ", pairList)  # Prints the list of pairs.

    except ValueError:
        print("Please enter a list structure: ", ValueError)
