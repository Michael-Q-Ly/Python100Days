"""
Hangman Game
"""
import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

"""

# TODO-1: Create a "placeholder" with the same number of blanks as letters
blank_list = []
for i in range(len(chosen_word)):
    blank_list.append('_')
print(*blank_list, sep='')

guess = input("Input a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the correct position
# in the blanks

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        blank_list[i] = guess
        print(*blank_list, sep='')
"""

# TODO-1: Create a "placeholder" with the same number of blanks as letters
placeholder = ''
for position in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

guess = input("Input a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the correct position
# in the blanks

display = ''
position = 0
for letter in chosen_word:
    if guess == letter:
        display += letter
    else:
        display += '_'

print(display)
