# Counts the total existing words of a paragraph.

def WordCounter():
    print("-----------------------------------------------")
    print("Counts the total existing words of a paragraph.")
    print("-----------------------------------------------")
    print()

    try:
        paragraph = input("Enter a paragraph: ")  # Stores a paragraph in a variable.

        # Converts the paragraph into a list. The elements are separated when a space is found.
        parag_words = paragraph.split()  

        word_count = 0  # Word count initialization.
        for x in parag_words:  # For every word it adds +1 to the count.
            word_count += 1

        print(f"Your paragraph has {word_count} words.")  # Prints the word counted.


    except ValueError:
        print("Enter a string paragraph: ", ValueError)
