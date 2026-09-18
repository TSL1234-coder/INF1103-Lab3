import sys

# Global variables
inventory = 0 
failed_attempts = 0

# ===========================
# Functions
# ===========================
def get_valid_input():
    
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    while user_input.lower() != 'quit':
        if not user_input.isdigit() or int(user_input) < 0:
            print("Error! Please enter a valid integer.")
            user_input = input("Enter stock quantity (or type 'quit' to exit): ")
            failed_attempts = failed_attempts + 1

        elif user_input.lower() == 'quit':
            generate_report(inventory, failed_attempts)
            return 'Quit'

        else:    
            return int(user_input)
        

def process_delivery(current_total, new_value):
    if new_value != None:
        current_total = current_total +  new_value

    return current_total


def calculate_tax(amount):
    tax_amount = amount * 0.1
    print("Tax amount: " + str(tax_amount))
    return tax_amount

def generate_report(total_units, rejected_entries):
    print("Inventory Report:")
    print("===================")
    print(f"Total Units Processed: {str(total_units)}")
    print(f"Total Rejected Entries: {str(rejected_entries)}")


# ===========================
# Calling Functions
# ===========================
while True:
    new_value = get_valid_input()
    process_delivery(inventory, new_value)
