import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        print("Error: Division by zero.")
        return None
    
    return num1 / num2



def start():
    print("""                         
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """)




start()

number_1 = float(input("What's the first number?: "))


while True:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")

    number_2 = float(input("What's the next number?: "))

    if operation == "+":
        total = add(number_1, number_2)
        print(f"{number_1} + {number_2} = {total}")

    elif operation == "-":
        total = sub(number_1, number_2)
        print(f"{number_1} - {number_2} = {total}")

    elif operation == "*":
        total = mul(number_1, number_2)
        print(f"{number_1} * {number_2} = {total}")

    elif operation == "/":
        total = div(number_1, number_2)
        print(f"{number_1} / {number_2} = {total}")
        if total == None:
            break
    
    more_operations = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
    if more_operations == "n":
        clear_terminal()
        start()
        number_1 = float(input("What's the first number?: "))
    else:
        number_1 = total
