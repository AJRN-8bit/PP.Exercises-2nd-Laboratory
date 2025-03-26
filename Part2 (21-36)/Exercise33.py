from Exercise28 import countries  # Imports the country list from the exercise 28

def CountryIndex():
    print("--------------------------------------------------------------")
    print("Finds the index of a country from the list of the exercise 28.")
    print("--------------------------------------------------------------")
    print()

    try:
        print("Countries: ",countries)  # Prints the countries
        print()

        country = input("Enter the country name: ")  # Saves the input country name.

        foundIndex = countries.index(country)  # Searches the index using the element name.

        if foundIndex != -1 or foundIndex != None:  # If the index is valid.
            print(f"Index of {country} is {foundIndex}.")

    except Exception as e: print("An error ocurred: ", e)
