from os import system  ## Imports the system 
from ExerciseSelection import OptionSelector

def main():

    x = True  # Initializes the while loop
    while(x == True):
        try:
            system("cls")  # Clears the console.

            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Select an exercise by entering its number. Use 0 to exit the program.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()

            option = int(input("Enter the number of the exercise (21 to 36): "))  # Selection of exercises
            system("cls") # Clears the console.

            if option == 0:  # Stops the loop
                print("Good bye.")
                x = False
                break

            OptionSelector(option)  # Selects the exercise from the "switch" structure.

            print()
            input("Press Enter to continue...")  # Lets the function show its messages.

        except ValueError:  # If an interger is not used.
            print("Please enter an interger and valid number. ", ValueError)


if __name__ == "__main__":  # It only executes when this file is runned.
    main()