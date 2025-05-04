from fruits import Fruit  # Import Fruit class from external file
import pickle  # For saving/loading data to a binary file
import os # For file path handling

# File name for saving the fruit list
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory where this file is located
FILENAME = os.path.join(script_dir, 'fruit_list.dat')    # Save file in same directory

def main():
    """
    Main loop of the application. Loads fruits, shows menu, and handles choices.
    """
    fruits = load_fruits()  # Try to load fruits from file
    if not fruits:
        fruits = create_startup_fruits()  # Load starter fruits if file is empty
    else:
        display_all_fruit_info(fruits)  # Show saved fruits at start

    # Loop forever until user chooses to exit
    while True:
        choice = get_menu_choice()  # Get user menu selection

        if choice == 1:
            add_fruit(fruits)  # Add new fruit
        elif choice == 2:
            print(f'Total fruits: {len(fruits)}')  # Show total fruits
        elif choice == 3:
            search_fruit(fruits)  # Search for a specific fruit
        elif choice == 4:
            print_fruit_names(fruits)  # List names of all fruits
        elif choice == 5:
            display_all_fruit_info(fruits)  # Show info about all fruits
        elif choice == 6:
            update_fruit(fruits)  # Update quantity/price of a fruit
        elif choice == 7:
            calculate_total_price(fruits)  # Calculate total value
        elif choice == 8:
            remove_fruit(fruits)  # Remove fruit from list
        elif choice == 9:
            fruits.clear()  # Clear all fruits
            print("All fruits cleared.")
        elif choice == 10:
            print('Exiting program...')
            break  # Exit the loop

        save_fruits(fruits)  # Save after every change

def get_menu_choice() -> int:
    """
    Display menu and return validated user input (1-10).
    """
    print("""
------------------------------------------------
Menu Options
------------------------------------------------
1. Add a fruit
2. Show number of fruits
3. Search for a fruit
4. List all fruit names
5. Show all fruit info
6. Update fruit quantity and price
7. Calculate total cost of all fruits
8. Remove a fruit by name
9. Clear all fruits
10. Exit program
------------------------------------------------
""")
    while True:
        try:
            val = int(input('Choose 1–10: '))
            if 1 <= val <= 10:
                return val
        except ValueError:
            pass
        print("Invalid input. Please enter a number between 1 and 10.")

def save_fruits(fruit_dict):
    """
    Save fruits to file using pickle.
    """
    with open(FILENAME, 'wb') as file:
        pickle.dump(fruit_dict, file)

def load_fruits():
    """
    Load fruits from file or return empty dict if not found.
    """
    try:
        with open(FILENAME, 'rb') as file:
            return pickle.load(file)
    except (IOError, EOFError):
        return {}

def create_startup_fruits():
    """
    Return a starter dictionary of fruits.
    """
    return {
        'Äpple': Fruit('Äpple', 6, 10),
        'Banan': Fruit('Banan', 5, 20),
        'Kiwi': Fruit('Kiwi', 10, 15)
    }

def add_fruit(fruit_dict):
    """
    Add a new fruit based on user input.
    """
    name = input('Name: ')
    if name in fruit_dict:
        print(f"{name} already exists.")
        return
    try:
        amount = int(input('Amount: '))
        price = float(input('Price: '))
        fruit_dict[name] = Fruit(name, amount, price)
        print(f"{name} added.")
    except ValueError:
        print("Invalid input. Amount must be integer, price must be float.")

def search_fruit(fruit_dict):
    """
    Search for a fruit and print it.
    """
    name = input('Enter fruit name to search: ')
    print(fruit_dict.get(name, 'Fruit not found.'))

def print_fruit_names(fruit_dict):
    """
    Print all fruit names.
    """
    for name in fruit_dict:
        print(name)

def display_all_fruit_info(fruit_dict):
    """
    Print full details for all fruits.
    """
    for fruit in fruit_dict.values():
        print(fruit)

def update_fruit(fruit_dict):
    """
    Update quantity and price for a fruit.
    """
    name = input('Enter fruit name to update: ')
    if name in fruit_dict:
        try:
            amount = int(input('New amount: '))
            price = float(input('New price: '))
            fruit = fruit_dict[name]
            fruit.amount = amount
            fruit.price = price
            print(f"Updated:\n{fruit}")
        except ValueError:
            print("Invalid input.")
    else:
        print(f"{name} not found.")

def calculate_total_price(fruit_dict):
    """
    Print total value of all fruits.
    """
    total = sum(fruit.price * fruit.amount for fruit in fruit_dict.values())
    print(f"Total cost of all fruits: {total:.2f} kr")

def remove_fruit(fruit_dict):
    """
    Remove a fruit by name.
    """
    name = input('Enter fruit name to remove: ')
    if name in fruit_dict:
        del fruit_dict[name]
        print(f"{name} removed.")
    else:
        print(f"{name} not found.")

if __name__ == "__main__":
    main()
