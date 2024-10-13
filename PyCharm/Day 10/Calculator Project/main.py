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


# TODO: Make a dictionary for these four values. Keys are +, -, *, and /
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}