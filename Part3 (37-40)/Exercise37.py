# Stores the names and grades in a dictionary as key-value.

def Store_NamesGrades():
    print("---------------------------------------------------------")
    print("Stores the names and grades in a dictionary as key-value.")
    print("---------------------------------------------------------")
    print()

    try:
        # Saves the amount of students that will be added.
        reps = int(input("Insert the number of students to register (interger): "))
        print()

        name_grade = {}  # Dictionary initialization.

        print("Enter name and grade (intergers) separated by spaces.")  # Message
        print()
 
        for x in range(1, reps +1):  # It asks data for every student. 
            data = list(input(f"Student {x}: ").split())  # Saves the name and grade as list.

            name = data[0]  # Stores the name.
            grade = int(data[1])  # Stores the grade.

            name_grade.update({name: grade})  # Adds the key and value to the dictionary.

        print()
        print("Student with his grade:")  # Message
        print()

        for key, value in name_grade.items():  # Prints all the keys and its values to view them in a better way.
            print(f"{key}: {value}")


    except ValueError as e:
        print("An error ocurred: ", e)
