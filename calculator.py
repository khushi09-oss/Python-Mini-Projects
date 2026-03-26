"""Simple command-line calculator.

This script asks the user for two numbers and an operation (+, -, x, /),
then calls `calculator(input1, input2, operation)` to perform the requested
calculation and print the result.

If an unsupported operation is provided, the function returns
"Invalid operation".
"""
def calculator(input1, input2, operation):
    if operation == '+':
        return input1 + input2
    elif operation == '-':
        return input1 - input2
    elif operation == '*':
        return input1 * input2
    elif operation == '%':
        if input2 != 0:
            return input1 % input2
        else:
            return "Error: Modulo by zero"
    elif operation == '**':
        return input1 ** input2 
    elif operation == '/':
        if input2 != 0:
            return input1 / input2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
    
while True:
    ent=input("Do you want to perform a calculation? (yes/no): ")
    if ent != "yes":
        break
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %, **): ")
    #function call 
    result = calculator(input1, input2, operation)
    print("Result:", result)