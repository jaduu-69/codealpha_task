"""
CodeAlpha - Task 1: Hangman Game
A text-based Hangman game with a limit of 6 incorrect guesses.

Author: <your name here>
"""

import random

# Word bank - feel free to add more words
WORD_BANK = [
    "python", "developer", "internship", "algorithm", "computer",
    "keyboard", "function", "variable", "database", "software"
]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
]


def choose_word():
    return random.choice(WORD_BANK)


def display_state(word, guessed_letters, wrong_count):
    print(HANGMAN_STAGES[wrong_count])
    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print("Word:", display_word)
    print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_count}")
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")


def get_guess(guessed_letters):
    while True:
        guess = input("\nGuess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_count = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} wrong guesses allowed.")
    print("=" * 40)

    while wrong_count < MAX_ATTEMPTS:
        display_state(word, guessed_letters, wrong_count)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            wrong_count += 1
            print("❌ Wrong guess!")

    # Player lost
    print(HANGMAN_STAGES[wrong_count])
    print(f"\n💀 Game Over! You've used all {MAX_ATTEMPTS} attempts.")
    print(f"The word was: '{word}'")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
