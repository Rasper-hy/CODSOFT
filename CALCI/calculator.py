# Simple Calculator - Task 2

print("Welcome to the Basic Calculator!\n")

# Getting inputs from the user
try:
    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Performing the calculation
    if operation == "+":
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nOops! You can't divide by zero.")
    else:
        print("\nInvalid operation selected. Please try again with +, -, *, or /.")
except ValueError:
    print("\nPlease enter valid numbers.")