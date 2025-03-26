# Counts the vocals that exists in a word.

def VocalCounter():
    print("----------------------------------------")
    print("Counts the vocals that exists in a word.")
    print("----------------------------------------")
    print()

    try:
        word = input("Enter a word: ")  # Stores the input string in a variable.

        conv_word = word.lower()  # Converts the word into lower case.

        sumVocals = 0  # Sum initialization.
        for x in conv_word:  # For every character in the word, it checks if its equal to a vocal.
            if x == 'a':
                sumVocals += 1

            elif x == 'e':
                sumVocals += 1

            elif x == 'i':
                sumVocals += 1

            elif x == 'o':
                sumVocals += 1

            elif x == 'u':
                sumVocals += 1

        print(f"The word: {word}, has {sumVocals} vocals.")  # Prints the word and its vocal count.



    except ValueError:
        print("Please enter a string: ", ValueError)
