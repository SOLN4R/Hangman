# Hangman by SOLN4R
# version 1.0: 25.11.2024
# version 1.01: 25.11.2024

import random
import string

# Constants
WORDS = [
    "python",
    "random",
    "function",
    "variable",
    "program",
    "developer",
    "debugging",
    "integer",
    "string",
    "algorithm",
]
MAX_TRIES = 6

def print_rules() -> None:
    """Print the game rules."""
    print("Welcome to Hangman!")
    print(f'''
Try to guess the hidden word one letter at a time.  
You have {MAX_TRIES} attempts. Each incorrect guess will cost you one attempt.  
Already guessed letters won't count, so choose carefully!  
If you reveal all the letters before your attempts run out, you win!  
Good luck and have fun!
''')


def get_user_guess(used_letters: set) -> str:
    """Get a valid letter from the user."""
    while True:
        try:
            user_input = input("Guess a letter: ").strip().lower()
            if len(user_input) != 1:
                raise ValueError("Input must be exactly one character.")
            if user_input not in string.ascii_lowercase:
                raise ValueError("Input must be a lowercase English letter.")
            if user_input in used_letters:
                raise ValueError("This letter has already been guessed.")
            return user_input
        except ValueError as e:
            print(f"[Error] {e}")


def play_game() -> None:
    """Play one round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_word = ["_"] * len(secret_word)
    used_letters = set()
    tries = 0

    print("A new word has been selected. Let’s start guessing!")

    while tries < MAX_TRIES:
        print("\n" + " ".join(guessed_word))
        print(f"Used letters: {', '.join(sorted(used_letters))}")
        print(f"Remaining attempts: {MAX_TRIES - tries}")

        guess = get_user_guess(used_letters)
        used_letters.add(guess)

        if guess in secret_word:
            print("Good job! The letter is in the word.")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
            if "_" not in guessed_word:
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                break
        else:
            print("Wrong guess! This letter is not in the word!")
            tries += 1
            if tries == MAX_TRIES:
                print(f"\nGame over! You’ve run out of attempts. The word was: {secret_word}")


def main() -> None:
    """Main function to manage the game loop."""
    print_rules()
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
