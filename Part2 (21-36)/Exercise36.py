from Exercise28 import countries  # Imports the country list from the exercise 28

def CountryCount():
    print("------------------------------------------------------------")
    print("Finds the total of countries in the list of the exercise 28.")
    print("------------------------------------------------------------")
    print()

    try:
        print("Countries: ",countries)  # Prints the countries
        print()

        totalCountries = len(countries)

        print("The total of countries found is: ", totalCountries)

    except Exception as e: print("An error ocurred: ", e)

