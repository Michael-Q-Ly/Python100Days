"""
Hangman Game
"""
import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# Select a word
chosen_word = random.choice(word_list)
print(chosen_word)

# Set the blank spaces for the user  to fill in
placeholder = ''
for position in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

# TODO-1: Use a while loop to let the user guess again

"""
Solution 1:
"""
# display = []
# while ''.join(display) != chosen_word:
#     guess = input("Input a letter: ").lower()
#
#     # TODO-2: Change the for loop so that you keep the previous correct letters
#     if len(display) != len(chosen_word):
#         for letter in chosen_word:
#             if guess == letter:
#                 display.append(guess)
#             else:
#                 display.append('_')
#     else:
#         for i in range(0, len(chosen_word)):
#             if guess == chosen_word[i]:
#                 display[i] = guess
#     print(''.join(display))

"""
Solution 2:
"""
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if '_' not in display:
        game_over = True
        print("You win!")
