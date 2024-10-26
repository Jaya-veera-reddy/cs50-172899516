import random
import sys

CAR_BRANDS = [
    "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
    "Nissan", "Hyundai", "BMW", "Mercedes-Benz", "Audi",
    "Subaru", "Kia", "Lexus", "Mazda", "Tesla",
    "Porsche", "Ferrari", "Jeep", "Volvo", "Jaguar"
]

def choose_word():
    return random.choice(CAR_BRANDS)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def is_word_guessed(word, guessed_letters):
    for letter in word.lower():
        if letter.lower() not in guessed_letters:
            return False
    return True

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman with Car Brands!")
    print(f"Try to guess the car brand with {len(word)} letters.")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word.lower():
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1

        if is_word_guessed(word, guessed_letters):
            print(f"\nCongratulations! You guessed the car brand '{word}'!")
            break

    if attempts == 0:
        print(f"\nOops! You ran out of attempts. The car brand was '{word}'.")

    sys.exit()  # Exit the program after finishing the game

if __name__ == "__main__":
    hangman()
