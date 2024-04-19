def miles_per_gallon(start_miles, end_miles, amount_gallons):
    miles_traveled = end_miles - start_miles
    mpg = miles_traveled / amount_gallons
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

def main():
    # Get user input for starting odometer, ending odometer, and fuel amount
    start_miles = float(input("Enter the starting odometer value in miles: "))
    end_miles = float(input("Enter the ending odometer value in miles: "))
    amount_gallons = float(input("Enter the amount of fuel in gallons: "))

    # Calculate miles per gallon
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Calculate liters per 100 kilometers from miles per gallon
    lp100k = lp100k_from_mpg(mpg)

    # Print the results
    print(f"\nFuel efficiency: {mpg:.1f} miles per gallon")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 kilometers")

# Call the main function to start the program
main()
