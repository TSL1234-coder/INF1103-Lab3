
# ===========================
# Functions
# ===========================

def get_valid_input():
    failed_attempts = 0

    while True:
        user_input = input(
            "Enter stock quantity (or type 'quit' to exit): "
        )

        if user_input.lower() == "quit":
            return "quit", failed_attempts

        if not user_input.isdigit() or int(user_input) < 0:
            print("Error! Please enter a valid integer.")
            failed_attempts += 1
        else:
            return int(user_input), failed_attempts


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax_amount = amount * 0.1
    return tax_amount


def generate_report(total_units, failed_attempts):
    print("\nInventory Report:")
    print("===================")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Total Rejected Entries: {failed_attempts}")


# ===========================
# Main Program
# ===========================

inventory = 0
total_deliveries = 0
failed_attempts = 0

while True:
    new_value, rejected = get_valid_input()

    failed_attempts += rejected

    if new_value == "quit":
        generate_report(total_deliveries, failed_attempts)
        break

    inventory = process_delivery(inventory, new_value)

    tax = calculate_tax(new_value)

    total_deliveries += 1

    print(f"Updated Inventory: {inventory}")
    print(f"Tax amount: ${tax:.2f}")