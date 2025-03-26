## Imports all the exercises
from Exercise1 import CheckAge
from Exercise2 import GradeChecker
from Exercise3 import UserIdentifier
from Exercise4 import GradeSearcher
from Exercise5 import FruitExists
from Exercise6 import LastnameSeparator
from Exercise7 import PairSum
from Exercise8 import ProducTable
from Exercise9 import SeparateElements1
from Exercise10 import SeparateElements2
from Exercise11 import PrintCharacters
from Exercise12 import PrintFigure1
from Exercise13 import PrintFigure2
from Exercise14 import ProductTable1to9
from Exercise15 import ShowElementsUntil1
from Exercise16 import ShowElementsUntil2
from Exercise17 import PairNumberSaver
from Exercise18 import VocalCounter
from Exercise19 import WordCounter
from Exercise20 import SumOfNumbers

def OptionSelector(option):
    try:
        # Saves all exercises match-case structure.
        match option:
            case 1: CheckAge()
            case 2: GradeChecker()
            case 3: UserIdentifier()
            case 4: GradeSearcher()
            case 5: FruitExists()
            case 6: LastnameSeparator()
            case 7: PairSum()
            case 8: ProducTable()
            case 9: SeparateElements1()
            case 10: SeparateElements2()
            case 11: PrintCharacters()
            case 12: PrintFigure1()
            case 13: PrintFigure2()
            case 14: ProductTable1to9()
            case 15: ShowElementsUntil1()
            case 16: ShowElementsUntil2()
            case 17: PairNumberSaver()
            case 18: VocalCounter()
            case 19: WordCounter()
            case 20: SumOfNumbers()
            case _: print("Not a valid option.")

    except Exception:
        print("An error ocurred", Exception)