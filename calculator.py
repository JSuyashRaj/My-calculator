def mycalculator():
    print("Enter first number")
    num1 = int(input())
    print("Enter second number")
    num2 = int(input())
    print("Enter an operator")
    operator = input()
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2) if num2 != 0 else print("Division by zero is not allowed")
    else:
        print("Invalid operator")