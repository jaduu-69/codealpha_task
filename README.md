# CodeAlpha - Hangman Game

A simple text-based Hangman game built in Python.

## Features
- Random word selection from a built-in word bank
- Visual ASCII hangman drawing that updates with each wrong guess
- Maximum of 6 incorrect guesses allowed
- Input validation (single letters only, no repeat guesses)
- Play again option

## How to Run
```bash
python hangman.py
```

## How It Works
1. The program randomly picks a word from `WORD_BANK`.
2. You guess one letter at a time.
3. Correct guesses reveal the letter in the word.
4. Incorrect guesses draw part of the hangman and use up one of your 6 attempts.
5. You win by guessing the full word before running out of attempts.

## Sample Output
```
Word: _ _ _ _ _ _
Wrong guesses left: 6
Guessed letters: None

Guess a letter: a
✅ Correct guess!
```

## Author
Internship Project - CodeAlpha
