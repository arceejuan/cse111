import csv
import random
import string
from datetime import datetime

def read_dictionary(filename, key_column_index):
    compound_dict = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) > key_column_index:
                key = row[key_column_index]
                compound_dict[key] = row
    return compound_dict

def generate_coupon(length=8):
    characters = string.ascii_letters + string.digits
    coupon = ''.join(random.choice(characters) for i in range(length))
    return coupon

def main():
    try:
        print("Juan Store\n")
        
        products_dict = read_dictionary("products.csv", 0)
        
        with open("request.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            
            total_items = 0
            subtotal = 0
            discounted = False
            
            print("Ordered Items:")
            print()
            
            coupons = []  # List to store generated coupons
            
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                
                current_day = datetime.now().strftime("%A")
                if current_day in ["Tuesday", "Wednesday"]:
                    product_price *= 0.90
                    discounted = True
                    print("Discount applied: 10% discount for Tuesday/Wednesday")
                
                current_time = datetime.now().time()
                if current_time < datetime.strptime("11:00", "%H:%M").time():
                    product_price *= 0.90
                    discounted = True
                    print("Discount applied: 10% discount before 11:00 a.m.")
                
                total_price = quantity * product_price
                total_items += quantity
                subtotal += total_price
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")
                
                # Generate coupon for one of the products ordered
                coupon = generate_coupon()
                coupons.append(coupon)
            
            print()
            
            print("Number of Items:", total_items)
            print("Subtotal: ${:.2f}".format(subtotal))
            
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            print("Sales Tax: ${:.2f}".format(sales_tax))
            
            total_due = subtotal + sales_tax
            print("Total: ${:.2f}".format(total_due))
            
            # Print generated coupon
            print("\nCoupon for one of the products ordered:", random.choice(coupons))
            print("Thank you for shopping at the Juan Store!")
            
            print("\nPlease take a moment to complete our online survey here https://survey.com")
            print("Your feedback is valuable to us.")
            
            current_date_and_time = datetime.now()
            print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))
            
    except FileNotFoundError:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: permission denied while accessing the file")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(repr(e))

if __name__ == "__main__":
    main()


