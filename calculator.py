import os
from time import sleep


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


try:
    while True:
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
(To exit please type 'exit')""")

        method = input("Which method would you like to use? ")
        if method == "exit":
            break
        elif method == "Exit":
            break
        elif method in ('1', '2', '3', '4'):
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))

            if method == "1":
                ans = add(num1, num2)
                print(f"{num1} + {num2} = {ans}")
                input("Press enter to continue...")
                clearConsole()
            elif method == "2":
                ans = subtract(num1, num2)
                print(f"{num1} - {num2} = {ans}")
                input("Press enter to continue...")
                clearConsole()
            elif method == "3":
                ans = multiply(num1, num2)
                print(f"{num1} x {num2} = {ans}")
                input("Press enter to continue...")
                clearConsole()
            elif method == "4":
                ans = divide(num1, num2)
                print(f"{num1} / {num2} = {ans}")
                input("Press enter to continue...")
                clearConsole()
        else:
            print("You did not choose a valid number.")
            sleep(1.8)

except SyntaxError:
    print("Syntax Error!")
except ValueError:
    print("Please enter a number next time!")
except ZeroDivisionError:
    print("You cannot divide by 0!")
