# Sum up to 3 interger numbers using a single function.

def SumOfNumbers():
    print("-----------------------------------------------------")
    print("Sum up to 3 interger numbers using a single function.")
    print("-----------------------------------------------------")
    print()

    try: 
        # Function inside a function that sums up to 3 numbers.
        def Sum(*nums):  # Takes al the parameters as a list.
            sum = 0  # Variable initialization.
            for x in nums:  # Every parameter in the list is added to the sum.
                sum += x

            return sum  # Returns the sum.
        

        # Asks for 3 interger numbers.
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        num3 = int(input("Number 3: "))

        sumRes = Sum(num1, num2, num3)  # Saves the return sum of the function into a variable.
        print(f"The sum of the numbers is: {sumRes}")  # Prints the sum.

    except ValueError:
        print("Please enter a list of interger numbers: ", ValueError)

