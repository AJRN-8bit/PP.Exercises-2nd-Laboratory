# Counts how many times a character appears in a string, using a dictionary.

def LetterCount():
    print("--------------------------------------------------------------------------")
    print("Counts how many times a character appears in a string, using a dictionary.")
    print("--------------------------------------------------------------------------")
    print()

    try:
        char_count = {}  # Dictionary initialization.

        word = input("Enter a word:")  # Stores the word in a variable.

        for char in word:  # Does the loop for every character in the word.

            if char in char_count:  # If a character exists in the dictionary it adds a +1 to its value.
                char_count[char] += 1
            
            else:  # If not, it adds the new char item to the dictionary.
                char_count.update({char: 1})
                 

        print()
        print("Char count dictionary: ")  # Message
        print()

        for key, value in char_count.items():  # Prints all the keys and its values to view them in a better way.
                print(f"{key}: {value}")


    except Exception as e:
        print("An error ocurred: ", e)
