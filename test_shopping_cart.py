# Initialize empty dictionaries for storing items, prices, and quantities
cart = {'items': [], 'prices': [], 'quantities': []}

# Function to add a new item to the cart
def add_item():
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item_name}'? $"))
    item_quantity = int(input(f"How many '{item_name}' would you like to add? "))
    
    # Check if the item is already in the cart
    if item_name in cart['items']:
        item_index = cart['items'].index(item_name)
        cart['quantities'][item_index] += item_quantity
    else:
        cart['items'].append(item_name)
        cart['prices'].append(item_price)
        cart['quantities'].append(item_quantity)
    
    print(f"{item_quantity} '{item_name}' {'have' if item_quantity > 1 else 'has'} been added to the cart.\n")

# Function to display the contents of the shopping cart
def display_cart():
    if not cart['items']:
        print("Your cart is empty.\n")
        return
    
    print("Your shopping cart:")
    print("{:<5} {:<20} {:<10} {:<10}".format("Index", "Item", "Quantity", "Price"))
    print("-" * 50)
    for index, (item, quantity, price) in enumerate(zip(cart['items'], cart['quantities'], cart['prices']), start=1):
        print("{:<5} {:<20} {:<10} ${:<10.2f}".format(index, item, quantity, price * quantity))
    print("-" * 50)
    print("{:<5} {:<20} {:<10} ${:<10.2f}\n".format("", "Total", sum(cart['quantities']), sum(cart['prices'])))

# Function to remove an item from the cart
def remove_item():
    if not cart['items']:
        print("Your cart is empty.")
        return
    
    display_cart()
    try:
        item_number = int(input("Enter the index of the item you want to remove: ")) - 1
        if 0 <= item_number < len(cart['items']):
            removed_item = cart['items'].pop(item_number)
            removed_price = cart['prices'].pop(item_number)
            removed_quantity = cart['quantities'].pop(item_number)
            print(f"{removed_quantity} '{removed_item}' {'have' if removed_quantity > 1 else 'has'} been removed from the cart.\n")
        else:
            print("Invalid item index. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid item index.\n")

# Main program loop
while True:
    print("Welcome to the Shopping Cart Program!\n")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Quit")
    
    try:
        choice = int(input("Please enter an action: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            display_cart()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
