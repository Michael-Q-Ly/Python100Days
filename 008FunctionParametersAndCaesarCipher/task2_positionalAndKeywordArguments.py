"""
Day 8 - Task 2 - Positional and Keyword Arguments
"""


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


if __name__ == "__main__":
    greet_with_name("Jack Bauer")

    # Testing Positional Arguments
    greet_with("Jack Bauer", "Nowhere")
    greet_with("Nowhere", "Jack Bauer")

    # Testing Keyword Arguments
    greet_with(location = "Paris, Texas", name = "Miggle")
