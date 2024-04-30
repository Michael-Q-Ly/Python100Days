#!/usr/bin/env/python
"""
Password generator project
Easy: No randomization of letters, numbers, and symbols
Hard: Total randomization of the above
"""

import random

__author__ = "Michael Ly"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Loop through randomly selected letters, numbers, and symbols and then
# concatenate them

alpha_chars = ''
for letter in range(0, nr_letters):
    alpha_chars += letters[random.randint(0, len(letters) - 1)]

number_chars = ''
for number in range(0, nr_numbers):
    number_chars += numbers[random.randint(0, len(numbers) - 1)]

symbol_chars = ''
for symbol in range(0, nr_symbols):
    symbol_chars += symbols[random.randint(0, len(symbols) - 1)]

password = alpha_chars + number_chars + symbol_chars
print("Your easy password is: " + password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Combine the strings to make it completely random!
password_list = []
for char in password:
    password_list += char

new_password = ''
# for char in range(0, len(password_list)):
# new_password += password_list[random.randint(0, len(password_array) - 1)]
# print('Your hard password is: ' + new_password)
# Above does not guarantee an index won't be picked again

# Do the same as above, but remove from the list
# Get the password length
# Loop through all of the password, removing a letter from the array at a time
password_length = nr_letters + nr_symbols + nr_numbers
for char in range(0, password_length):
    # To do this, we need a storage unit for the index
    password_index = random.randint(0, len(password_list) - 1)
    new_password += password_list[password_index]
    # We then remove the index and update the array so that it removes used
    # letters and gets a new size
    password_list.remove(password_list[password_index])
print("Your hard password is: " + new_password)

'''
Angela Yu's way of doing it:
'''

# Create a list from the original password
password_list = []
for char in password:
    password_list += char
# Shuffle the list
random.shuffle(password_list)

# Reset the password and store the list into the string variable
password = ''
for char in password_list:
    password += char
print(f"password: {password}")
