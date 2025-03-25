def calculator():
    print("Welcome to the Basic Calculator!")
    
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter an another number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    operator = input("Enter an operator (+, -, *, /, %): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        print("Invalid operator! Please enter one of +, -, *, /, %.")
        return

    print(f"The result of {num1} {operator} {num2} is: {result}")
    
if __name__ == "__main__":
    calculator()