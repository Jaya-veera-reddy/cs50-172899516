import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError("Please enter a positive integer.")
            break
        except ValueError as ve:
            print(ve)

    target_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError("Please enter a positive integer.")

            if guess < target_number:
                print("Too small!")
            elif guess > target_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    main()
