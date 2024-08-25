"""
Day 8 - Functions with inputs
"""


def greet():
    print("Hello, World!")
    print("It's really hot in Texas!")
    print("We have triple-digit weather all month!")


def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How do you do, {name}?")


if __name__ == '__main__':
    greet()
    greet_with_name("Michael")
