# Prints the highest and lowest number in an int list.

def GradeSearcher():
    print("----------------------------------------------------")
    print("Prints the highest and lowest number in an int list.")
    print("----------------------------------------------------")
    print()

    try:
        # Stores the input of intergers in a list.
        gradeList = list(map(int, input("Enter grades (separated by spaces): ").split()))
        
        maxGrade = max(gradeList)  # Searches for the highest int value and stores it in a variable.
        minGrade = min(gradeList)  # Searches for the lowest int value and stores it in a variable.

        print(f"The highest grade is: {maxGrade}, and the lowest is: {minGrade}.") # Prints the result.

    except ValueError:  # If the input are not intergers.
        print("Invalid input.", ValueError)
