# guess_the_word.py
import random

def choose_word():
    """Select a random word from a predefined list."""
    words = ["python", "github", "pytest", "banana", "hangman"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the current progress of the guessed word."""
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Guess the Word!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and set(word) != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect. {attempts} attempts left.")

        print(display_word(word, guessed_letters))

    if set(word) == guessed_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Out of attempts! The word was: {word}")

if __name__ == "__main__":
    play_game()