## Technical Specification (TZ)

### Project Description
Hangman is a console game where the program selects a random word, and the player attempts to guess it by entering letters. The player wins if they guess the word before exhausting their attempts.

---

### Functional Requirements
- The program randomly selects a word from a predefined list.
- The word is displayed as a series of underscores (`_`), representing each letter in the word.
- The player inputs one letter at a time.
- The program validates the input:
  - Ensures the input is a single lowercase English letter.
  - Checks if the letter has already been guessed and provides appropriate feedback.
- After each guess:
  - If the guessed letter is in the word, the program reveals all occurrences of that letter.
  - If the guessed letter is not in the word, the number of remaining attempts decreases.
- The game ends when:
  - The player successfully guesses the entire word (win).
  - The player runs out of attempts (loss).
- The program displays:
  - The current progress of the word (e.g., `_ p p _ e`).
  - The list of already guessed letters.
  - The number of remaining attempts.
- After the game ends, the program offers the player the option to play again.

---

### Non-Functional Requirements
- The code is written in Python 3.7 or higher.
- The game operates through a console-based interface.
- The code is modular, using functions to separate logic and improve readability.
- The program handles invalid inputs gracefully, without crashing.
- The word list is easily extendable.

---

### Technical Constraints
- Players have a maximum of 6 attempts to guess the word.
- The word list contains at least 10 words.

---

### Python Topics Used
- **Random module**: For selecting a random word.
- **Strings and lists**: To store the word and track progress.
- **While loops**: For the main game loop.
- **Conditional statements**: To manage game logic.
- **Exception handling**: To handle invalid input via `try-except`.
- **Functions**: To organize the code into reusable blocks.
- **String formatting**: To dynamically generate user-friendly messages.

---

### Example Gameplay
1. Random word: `apple`.  
   Initial display: `_ _ _ _ _`.  

2. Player enters `a`.  
   Updated display: `a _ _ _ _`.

3. Player enters `z`.  
   Feedback: "Wrong guess! This letter is not in the word! Attempts remaining: 5".

4. The player continues guessing until they either win or lose.
