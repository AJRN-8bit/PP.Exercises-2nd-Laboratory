# Stores the words of a paragraph by word size in dictionary as key-set.

def WordLenght():
    print("----------------------------------------------------------------------")
    print("Stores the words of a paragraph by word size in dictionary as key-set.")
    print("----------------------------------------------------------------------")
    print()

    try:
        # Saves an entered paragraph.
        paragraph = input("Enter a paragraph: ")
        print()

        word_length_set = {}  # Dictionary initialization.
 
        words = paragraph.split()  # Converts the paragraph in a list of words.

        words = [word.lower() for word in words]  # Converts all the words to lowercase.

        # Removes the special characters from the paragraph. Help from AI.
        words = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in paragraph).split()


        for word in words:  # Iterates over the list of words.
             
            if len(word) in word_length_set:
                # Takes the length of the word as key and adds a word to the set if it matches the key.
                # Creates an automatic set.
                word_length_set[len(word)].add(word)  

            else: # If the lenght key doesnt exists, it adds a new key an the current word.
                word_length_set.update({len(word): {word}})


        word_length_set = dict(sorted(word_length_set.items(), reverse= False))  # Sorts the dictionary keys in ascending order.

        print()
        print("Created dictionary: ")  # Message
        print()

        for key, _set in word_length_set.items():  # Prints all the keys and its values to view them in a better way.
                print(f"{key}: {_set}")


    except Exception as e:
        print("An error ocurred: ", e)
