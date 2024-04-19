# I included hints that would indicate if there is a letter from the initial guess is correct, I denoted it with in lowercase. Otherwise,
# if the correct position of a letter from the guess is also correct, I denote it in uppercase and put it in the correct position, I also made
# sure that there is a correct prompt whenever the user inputs an incorrect number of letters for a guess.


import random

def generate_hint(secret_word, guess):
    hint = []
    for sw, gw in zip(secret_word, guess):
        if sw == gw:
            hint.append(sw.upper())
        elif gw in secret_word:
            hint.append(gw.lower())
        else:
            hint.append('_')
    return ' '.join(hint)

def main():
    words = ['mosiah', 'alma', 'nephi', 'helaman', 'mormon', 'moroni', 'abinadi', 'teancum', 'ether', 'zeniff']
    secret_word = random.choice(words)
    word_length = len(secret_word)
    hint = ['_'] * word_length
    guesses = 0

    print("Welcome to the word guessing game!")
    print(f"Your hint is: {' '.join(hint)}")

    while True:
        guess = input("What is your guess? ").lower()

        if len(guess) != word_length:
            print("Sorry, the guess must have the same number of letters as the secret word.")
            guesses += 1
            continue

        guesses += 1
        if guess == secret_word:
            print(f"Congratulations! You guessed it!\nIt took you {guesses} guesses.")
            break
        else:
            hint = generate_hint(secret_word, guess)
            print(f"Your hint is: {hint}")

if __name__ == "__main__":
    main()
