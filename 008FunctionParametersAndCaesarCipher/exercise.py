"""
Day 8 - Exercise 1
Create a function called life_in_weeks() using math and f-strings that tell us
how many weeks we have left if we live until 90 years old

Your current age will be taken as input and output a message with our time left
in this format:
    You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age
has left until age 90
"""


def life_in_weeks(age_in_years):
    WEEKS_IN_A_YEAR = 52
    total_weeks = 90 * 52   # 90 years * 52 weeks
    age_in_weeks = age_in_years * WEEKS_IN_A_YEAR
    weeks_left = total_weeks - age_in_weeks
    return weeks_left


if __name__ == "__main__":
    time_left = life_in_weeks(int(input("How many years old are you? ")))
    print(f"You have {time_left} weeks left.")
