## Imports all the exercises
from Exercise21 import ListUsage1
from Exercise22 import ListUsage2
from Exercise23 import ListUsage3
from Exercise24 import Error1
from Exercise25 import Error2
from Exercise26 import Error3
from Exercise27 import LetterFinding
from Exercise28 import FindCountries
from Exercise29 import AddListElements
from Exercise30 import PopListElements
from Exercise31 import CreateListCopy
from Exercise32 import RepeatedValues
from Exercise33 import CountryIndex
from Exercise34 import Sort_StoL
from Exercise35 import Sort_LtoS
from Exercise36 import CountryCount


def OptionSelector(option):
    try:
        # Saves all exercises match-case structure.
        match option:
            case 21: ListUsage1()
            case 22: ListUsage2()
            case 23: ListUsage3()
            case 24: Error1()
            case 25: Error2()
            case 26: Error3()
            case 27: LetterFinding()
            case 28: FindCountries()
            case 29: AddListElements()
            case 30: PopListElements()
            case 31: CreateListCopy()
            case 32: RepeatedValues()
            case 33: CountryIndex()
            case 34: Sort_StoL()
            case 35: Sort_LtoS()
            case 36: CountryCount()
            case _: print("Not a valid option.")

    except Exception:
        print("An error ocurred", Exception)