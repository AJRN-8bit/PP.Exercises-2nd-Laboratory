# Deletes specific values of a dictionary.

def DeleteSpecificNumbers():
    print("----------------------------------------")
    print("Deletes specific values of a dictionary.")
    print("----------------------------------------")
    print()

    try:
        ori_dictionary = {
            "num1": -42,
            "num2": 18,
            "num3": 56,
            "num4": -7,
            "num5": 33,
            "num6": -19,
            "num7": 101,
            "num8": -88,
            "num9": 24,
            "num10": 67,
            "num11": -14,
            "num12": 90,
            "num13": -36,
            "num14": 72,
            "num15": -5
        }

        for key, value in ori_dictionary.items():  # Prints all the keys and its values to view them in a better way.
            print(f"{key}: {value}")

        print()
        option = int(input("Enter [1] to only view the positive numbers or [2] to only view the negative ones: "))
        # Stores the option in a variable.
        print()

        alter_dictionary = {}  # Dictionary initialization.

        if option == 1 or 2:  # If the option is 1 or 2
            if option == 1:  # If the option is 1 it show only the positive items.
                alter_dictionary = {k: v for k, v in ori_dictionary.items() if v > 0}

            elif option == 2:  # If the option is 2 it show only the negative items. 
                alter_dictionary = {k: v for k, v in ori_dictionary.items() if v < 0} 

            print("Updated dictionary: ")  # Message
            print()
            
            for key, value in alter_dictionary.items():  # Prints all the keys and its values to view them in a better way.
                print(f"{key}: {value}")

        else:
            print("Invalid option.")


    except Exception as e:
        print("An error ocurred: ", e)
