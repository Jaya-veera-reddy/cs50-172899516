    # Hangman game for guessing car brand
    #### Video Demo:  https://youtu.be/POn7FKvHPEc
    #### Description:

THangman Game with Car Brands
This code presents a straightforward implementation of the Hangman game, using popular car brands as the words to guess. The main goal is to successfully identify the car brand by guessing letters within a limited number of attempts.

How to Play:
Initialization:

The game begins by randomly selecting a car brand from the predefined list CAR_BRANDS.
The chosen word is initially hidden from the player, who only knows the number of letters in the word.
Guesses and Attempts:

The player has six attempts to guess the entire word.
Each incorrect guess reduces the number of remaining attempts by one.
Displaying Progress:

The game displays the word with underscores (_) representing the letters that have not been guessed yet.
Correctly guessed letters are revealed in their respective positions, helping the player see their progress.
Player Input:

The player inputs one letter at a time as a guess.
The game checks whether the guessed letter has already been guessed or if it is present in the word.
Feedback:

For each guess, the game provides immediate feedback.
If the guess is correct, the game congratulates the player and updates the display.
If the guess is incorrect, the game informs the player and decreases the number of remaining attempts by one.
Winning or Losing:

The player wins if they correctly guess all the letters in the word within the allowed attempts.
The player loses if they run out of attempts before guessing the word.
Game Over:

Once the game concludes, whether the player wins or loses, it reveals the correct car brand.
The program then exits.
Example Gameplay:
At the start, the game randomly selects a car brand, such as "Toyota".
The display shows _ _ _ _ _ _, with six underscores representing the six letters in "Toyota".
The player guesses a letter, for example, 't'.
If 't' is in the word, the display updates to T _ _ _ _ t.
The player continues to guess letters, trying to fill in the blanks.
The game proceeds with the player making guesses until they either guess the entire word or exhaust their attempts.

Detailed Code Explanation:
The code uses Python's random module to select a word randomly from the list of car brands. Here is a breakdown of the main functions and their roles in the game:

choose_word():



def choose_word():
    return random.choice(CAR_BRANDS)
This function randomly selects and returns a car brand from the list.
display_word(word, guessed_letters):



def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
This function constructs the current state of the word to be displayed. It shows the correctly guessed letters and underscores for the remaining letters.
is_word_guessed(word, guessed_letters):


def is_word_guessed(word, guessed_letters):
    for letter in word.lower():
        if letter.lower() not in guessed_letters:
            return False
    return True
This function checks if the player has guessed all the letters in the word.
hangman():


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

    sys.exit()
This is the main game function. It handles the game logic, including initializing variables, processing player guesses, providing feedback, and determining the game's outcome.


The Hangman game implementation offers a fun and engaging way to test your knowledge of car brands. By guessing letters and revealing parts of the word progressively, players can enjoy a classic game while learning or recalling various car brands. This simple yet entertaining game is a great way to pass the time and challenge yourself or friends.
