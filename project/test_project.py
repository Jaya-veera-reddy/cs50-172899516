import pytest
from project import choose_word, display_word, is_word_guessed

def test_choose_word():
    car_brands = [
        "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
        "Nissan", "Hyundai", "BMW", "Mercedes-Benz", "Audi",
        "Subaru", "Kia", "Lexus", "Mazda", "Tesla",
        "Porsche", "Ferrari", "Jeep", "Volvo", "Jaguar"
    ]
    chosen_word = choose_word()
    assert chosen_word in car_brands

def test_display_word():
    word = "Toyota"
    guessed_letters = ['o', 't', 'y']
    displayed = display_word(word, guessed_letters)
    assert displayed == "Toyot_"

def test_display_word_no_guesses():
    word = "Honda"
    guessed_letters = []
    displayed = display_word(word, guessed_letters)
    assert displayed == "_____"

def test_display_word_all_guessed():
    word = "BMW"
    guessed_letters = ['b', 'm', 'w']
    displayed = display_word(word, guessed_letters)
    assert displayed == "BMW"

def test_is_word_guessed():
    word = "Ford"
    guessed_letters = ['f', 'o', 'r', 'd']
    assert is_word_guessed(word, guessed_letters) == True

def test_is_word_not_guessed():
    word = "Chevrolet"
    guessed_letters = ['c', 'h', 'e', 'v']
    assert is_word_guessed(word, guessed_letters) == False

def test_is_word_empty_guesses():
    word = "Nissan"
    guessed_letters = []
    assert is_word_guessed(word, guessed_letters) == False

if __name__ == "__main__":
    pytest.main()

