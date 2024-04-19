#Tire Volume by Arcee Juan
import math

from datetime import datetime

current_date_and_time = datetime.now()

#Input from the user
tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): " ))

#Compute the tire volume
volume = (math.pi * (tire_width ** 2) * aspect_ratio * ((tire_width * aspect_ratio) + (2540 * diameter))) / 10000000000

print(f" \nThe approximate volume is {volume: .2f} liters")


if 195 <= tire_width <= 205 and 55 <= aspect_ratio <= 65 and diameter == 15:
    tire_price = 150
elif 215 <= tire_width <= 225 and 60 <= aspect_ratio <= 70 and diameter == 16:
    tire_price = 180
elif 235 <= tire_width <= 245 and 65 <= aspect_ratio <= 75 and diameter == 17:
    tire_price = 200
else:
    tire_price = 0

if tire_price > 0:
    print(f"\n Tire Price: ${tire_price}")
else:
    print("\n Sorry, the tire price is not available for the entered dimensions.")

purchase_tires = input("\nDo you want to buy tires with the entered dimensions? (yes/no): ")

if purchase_tires == "yes":
    user_name = input("Please enter your name: ")
    user_contact_number = input("Please enter your phone numer: ")

    with open("volumes.txt", "at") as tire_volumes:
        print(f"{current_date_and_time: %Y-%m-%d}, {int(tire_width)}, {int(aspect_ratio)}, {int(diameter)}, {volume: .2f}, {user_name}, {user_contact_number}", file=tire_volumes)
        print(f"\nThank you {user_name}! Your information with your phone number has been recorded.")

else:
    print("\nThank you for using the tire volume calculator!")

input("\nPlease press Enter to exit")