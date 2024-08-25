"""
Day 8
Love Calculator
Write a function called calculate_love_score() that tests the compatibility
between two names.
To work out  the love score between two people:
    1. Take both names and check for the number of times the letters in the word
    TRUE occurs
    2. Then check for the number of times the letterse in the  word LOVE
    occurs
    3. Then combine these numbers to make a 2-digit number and print it
    out
    E.G.:
    name 1 = "Angela Yu" name2 = "Jack Bauer"
    T occurs 0 times
    R occurs 1 times
    U occurs 2 times
    E occurs 2 times
    Total = 5
    L occurs 1 time
    O occurs 0 times
    V occurs 0 times
    E occurs 2 times
    Total = 3

    Love score = 53

Example input:
    calculate_love_score("Kanye West", "Kim Kardashian")
"""

love_string_1 = "TRUE"
love_string_2 = "LOVE"


def calculate_love_score(name1, name2):
    # Change all names to uppercase to compare against the all-uppercase love strings
    name1 = name1.upper()
    name2 = name2.upper()
    # Combine the names into a single string so we can compare all at once
    combined_names = name1 + name2

    # 1. Get the points for TRUE section
    true_points = 0
    # We need to obtain letter points and print them out
    for letter in love_string_1:
        letter_points = 0

        for name_letter in combined_names:
            if letter == name_letter:
                letter_points += 1

        print(f"{letter} occurs {letter_points} times")

        true_points += letter_points
    print(f"Total = {true_points}")

    # Get the points for LOVE section
    love_points = 0
    for letter in love_string_2:
        letter_points = 0

        for name_letter in combined_names:
            if letter == name_letter:
                letter_points += 1

        print(f"{letter} occurs {letter_points} times")

        love_points += letter_points
    print(f"Total = {love_points}")

    true_love_score = str(true_points) + str(love_points)
    print(f"Love Score = {true_love_score}")


if __name__ == "__main__":
    name1 = "Angela Yu"
    name2 = "Jack Bauer"
    calculate_love_score(name1, name2)
