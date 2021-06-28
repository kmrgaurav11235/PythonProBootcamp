# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    continue_calculating = "y"
    num1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    while continue_calculating.lower() == "y":
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
    else:
        calculator()

        
calculator()