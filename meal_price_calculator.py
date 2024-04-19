# I added the feature of asking the price of drinks, appetizers, and the tip percentage. In the end of the program, calculation of the total bill and a separate computation of how much tip was payed is also displayed.

# Function to format currency with two decimal places
def format_currency(amount):
    return "${:.2f}".format(amount)

# Function to calculate the tip
def calculate_tip(total_price, tip_percentage):
    return total_price * tip_percentage / 100

# Ask for the price of a child's meal
child_price = float(input("What is the price of a child's meal? "))

# Ask for the price of an adult's meal
adult_price = float(input("What is the price of an adult's meal? "))

# Ask for the number of children
num_children = int(input("How many children are there? "))

# Ask for the number of adults
num_adults = int(input("How many adults are there? "))

# Ask for the price of drinks
drink_price = float(input("What is the price of drinks? "))

# Ask for the price of appetizers
appetizer_price = float(input("What is the price of appetizers? "))

# Ask for the tip percentage
tip_percentage = float(input("What is the tip percentage? "))

# Determine the meal's subtotal
subtotal = (child_price * num_children) + (adult_price * num_adults) + drink_price + appetizer_price

# Display the subtotal
print("\nSubtotal:", format_currency(subtotal))

# Ask for the sales tax rate and store as a floating point number
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Compute and display the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100
print("Sales Tax:", format_currency(sales_tax))

# Compute and display the total price of the meal
total_price = subtotal + sales_tax
print("Total:", format_currency(total_price))

# Calculate and display the tip
tip_amount = calculate_tip(total_price, tip_percentage)
print("Tip:", format_currency(tip_amount))

# Ask for the payment amount and store as a floating point number
payment_amount = float(input("\nWhat is the payment amount? "))

# Compute and display the change
change = payment_amount - total_price - tip_amount
print("Change:", format_currency(change))
