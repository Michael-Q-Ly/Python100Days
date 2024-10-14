"""
#!/user/bin/env python
Calculator
Performs addition, subtraction, multiplication, and division.
Allows the user to use previous result for additional operations or to start
over from scratch.
"""


def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts the second number from the first number"""
    return n1 - n2


def multiply(n1, n2):
    """Multiples two numbers together"""
    return n1 * n2


def divide(n1, n2):
    """Divides the first number by the second number"""
    return n1 / n2


def main():
    """Calculator program"""

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    result = None
    use_previous_result = False
    while True:
        if not use_previous_result:
            num1 = float(input("Please input the first number: "))
        else:
            num1 = result

        operator = input(f"PLease input the operation to use on {num1}: ")

        num2 = float(input("Please input the second number: "))

        result = operations[operator](num1, num2)
        print(f"Your result is {result}")

        request_continuation = input("Would you like to continue with this "
                                     "result as your first number ("
                                     "y/N)? ").lower()

        if request_continuation in ('y', 'yes'):
            use_previous_result = True
            num1 = result
        elif request_continuation in ('n', 'no'):
            use_previous_result = False
            continue
        else:
            print("You must enter 'y' or 'n'")


if __name__ == '__main__':
    main()
