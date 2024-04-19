secret_word = 'mosiah'
num_guesses = 0

print("Welcome to the word guessing game!")

while True:
    guess = input("What is your guess? ").lower()
    num_guesses += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {num_guesses} guesses.")
        break
    else:
        print("Your guess was not correct.")
