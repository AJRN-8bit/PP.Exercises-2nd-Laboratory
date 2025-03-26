# Evaluates a grade and prints a message.

def GradeChecker():
    print("----------------------------------------------")
    print("Evaluates an input grade and prints a message.")
    print("----------------------------------------------")
    print()

    try:
        grade = int(input("Enter your current grade (interger): "))  # It converts the string into an int and stores it in a variable.

        # Every if or elif structure check the grande on a range of grades.
        if grade >= 0 and grade < 5:
            print("Suspended.")

        elif grade >= 5 and grade < 6:
            print("Enough.")

        elif grade >= 6 and grade < 7:
            print("Good.")

        elif grade >= 7 and grade < 9:
            print("Notable.")

        elif grade >= 9 and grade < 10:
            print("Excellent.")

        else:  # If the grade is less than 0 or greater than 10.
            print("Not a valid grade.")

    except ValueError:  # If an error occures.
        print("Please enter an interger. ", ValueError)