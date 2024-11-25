# Hangman by SOLN4R
# version 1.0: 25.11.2024

import random
import string

words = [
    "python",
    "random",
    "function",
    "variable",
    "program",
    "developer",
    "debugging",
    "integer",
    "string",
    "algorithm"
]

QUANTITY_WORDS = len(words)
letters_used = []
MAX_TRIES = 6

def print_rules() -> None:
    print("Welcome to Hangman!")
    print(f'''
Try to guess the hidden word one letter at a time.  
You have 6 attempts. Each incorrect guess will cost you one attempt.  
Already guessed letters won't count, so choose carefully!  
If you reveal all the letters before your attempts run out, you win!  
Good luck and have fun!
''')

def get_user_guess() -> str:
    while True:
        try:
            user_input = input("Guess a letter: ").strip()
            if len(user_input) != 1:
                raise ValueError("Input must be exactly one character.")
            if user_input not in string.ascii_lowercase:
                raise ValueError("Input must be a lowercase English letter.")
            if user_input in letters_used:
                raise ValueError("This letter has already been guessed.")

            letters_used.append(user_input)
            return user_input

        except ValueError as e:
            print(f"[Error] {e}")


def play_game() -> None:

    letters_used.clear()
    tries = 0
    secret_word = words[random.randrange(QUANTITY_WORDS)]
    guessed_word = ["_"] * len(secret_word)
    print("A new word has been selected. Let’s start guessing!")

    while True:
        print("\n")
        print(" ".join(guessed_word))

        if "".join(guessed_word) == secret_word:
            print("Congratulations! You guessed the word!")
            break
        temp = "".join(guessed_word)
        guess = get_user_guess()

        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess

        if temp == "".join(guessed_word):
            tries += 1
            print(f"Wrong guess! This letter is not in the word! Attempts remaining: {MAX_TRIES - tries}")
            if tries == 6:
                print(f"Game over! You’ve run out of attempts. The word was: {secret_word}")
                break
        else:
            print("Good job! The letter is in the word.")

def main() -> None:
    while True:
        print_rules()
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()