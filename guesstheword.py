import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

display = []
for _ in range(len(chosen_word)):
    display += "_"

won = False
attempts = 0

while won is not True:
    guess = input("Guess a letter: ").lower()
    attempts += 1

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if "_" not in display:
        print("You win!")
        won = True

print(f'Attempts: {attempts}')
