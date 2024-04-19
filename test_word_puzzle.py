import random

# Define the secret word
secret_word = "mosiah"
secret_word_length = len(secret_word)

# Initialize variables
guesses = 0
correct_guess = False
hint = ['_'] * secret_word_length

print("Welcome to the word guessing game!\n")

while not correct_guess:
    print("Your hint is:", ' '.join(hint))
    user_input = input("What is your guess? ").lower()

    # Check if the guess has the same number of letters as the secret word
    if len(user_input) != secret_word_length:
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        guesses += 1
        continue

    guesses += 1

    # Check for correct letters and positions
    for idx, letter in enumerate(user_input):
        if letter == secret_word[idx]:
            hint[idx] = letter.upper()
        elif letter in secret_word:
            if letter.lower() not in hint:
                hint[secret_word.index(letter)] = letter.lower()

    # Check if the guess is correct
    if ''.join(hint) == secret_word:
        correct_guess = True
        print(f"Congratulations! You guessed it!\nIt took you {guesses} guesses.")
    else:
        print("Your hint is:", ' '.join(hint), "\n")
