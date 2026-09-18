import sys

inventory = 0 


def get_valid_input():
    
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    while user_input.lower() != 'quit':
        if user_input.lower() == 'quit':
                return 'Quit'
                sys.exit()
        elif not user_input.isdigit() or int(user_input) < 0:
                print("Error! Please enter a valid integer.")
                user_input = input("Enter stock quantity (or type 'quit' to exit): ")
                # failed_attempts +=1
        else:
                # pass user_input value to process_delivery()
                return int(user_input)
        

def process_delivery(quantity):
    print(quantity)


get_valid_input()
process_delivery(get_valid_input())