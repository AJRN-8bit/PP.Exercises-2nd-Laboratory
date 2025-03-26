## Imports all the exercises
from Exercise37 import Store_NamesGrades
from Exercise38 import DeleteSpecificNumbers
from Exercise39 import LetterCount
from Exercise40 import WordLenght


def OptionSelector(option):
    try:
        # Saves all exercises match-case structure.
        match option:
            case 37: Store_NamesGrades()
            case 38: DeleteSpecificNumbers()
            case 39: LetterCount()
            case 40: WordLenght()
            case _: print("Not a valid option.")

    except Exception:
        print("An error ocurred", Exception)