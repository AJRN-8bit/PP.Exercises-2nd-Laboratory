# Prints every caracter of a string using a for loop.

def PrintCharacters():
    print("---------------------------------------------------")
    print("Prints every caracter of a string using a for loop.")
    print("---------------------------------------------------")
    print()

    try:
        word = input("Enter a word: ")  # Stores the string input in a variable.

        for char in word:  # It does the loop for each existing character in the word.
            print(char, end=" ")  # Print in a single line all the characters.

    except ValueError:  # If the input is not a string shows an error.
        print("Please use a string: ", ValueError)
