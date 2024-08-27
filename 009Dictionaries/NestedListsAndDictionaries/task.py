"""
Day 9
Nested lists and dictionaries
"""
capitols = {
    "France": "Paris",
    "Germany": "Berlin",
}
"""
# Nested list in dictionary:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Challenge/Quiz: Print out "Lille" from the dictionary above
# [Sol]:
# Pass key to dictionary to get value. Then select the index after the square bracket
# for the key is closed. E.g., dictionary[key][index]
# To break it down, dictionary[key] transforms into a list. (list)[index]
print(travel_log["France"][1])
"""

# Challenge/Quiz: Print out "D" from the nested list below
nested_list = ["A", "B", ["C", "D"]]
# [Sol]
# Get the index of the list in the outer list. You are now addressing another list.
# Add a new square bracket for the inner list to address the index of D now
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
}

# Challenge/Quiz: Print out "Stuttgart" from the above nested dictionary
# [Sol]
# dictionary[key_dictionary][key_dictionary_list][key_dictionary_list_index]
print(travel_log["Germany"]["cities_visited"][2])
