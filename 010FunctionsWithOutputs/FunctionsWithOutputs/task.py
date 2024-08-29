"""
Day 10
Functions with Outputs
"""

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


def function_1(text):
    return text + text

def function_2(text):
    return text.title()


if __name__ == "__main__":
    print(format_name("mIcHael", "mICHaEL"))

    output = function_2(function_1("hello"))
    print(output)
