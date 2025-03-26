# Stores the word and its lenght in a dictionary as key-value.

def WordLenght():
    print("------------------------------------------------------------")
    print("Stores the word and its lenght in a dictionary as key-value.")
    print("------------------------------------------------------------")
    print()

    try:
        # Saves the amount of words to evaluate.
        wordsAmount = int(input("Insert the number of words to register (interger): "))
        print()

        word_length = {}  # Dictionary initialization.

        print("Enter word: ")  # Message
        print()
 
        words = []  # List initialization.

        for x in range(1, wordsAmount +1):  # It asks the word the amount of times requestes. 
            word = input(f"Word {x}: ")  # Saves the name and grade as list.
            words.append(word)  # Adds the word to the words list.


        for word in words:  # Make a loop for every word in the word list.

            lenght = ""  # Lenght initialization.
            for n in range(1, len(word)+1):  # It makes the loop for the lenght of the word.
                x = str(n)  # Converts the current number loop into a string.
                lenght += x  # Adds the number to the empty string.

            word_length.update({word: lenght})  # Adds the key and value to the dictionary.

        print()
        print("Create dictionary: ")  # Message
        print()

        for key, value in word_length.items():  # Prints all the keys and its values to view them in a better way.
                print(f"{key}: {value}")


    except Exception as e:
        print("An error ocurred: ", e)
