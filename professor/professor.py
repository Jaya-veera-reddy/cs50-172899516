import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        correct_answer = X + Y

        tries = 0
        while tries < 3:
            try:
                answer = int(input(f"{X} + {Y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    tries += 1
                    if tries < 3:
                        print("EEE")
                    else:
                        print(f"Correct answer: {correct_answer}")
            except ValueError:
                tries += 1
                if tries < 3:
                    print("EEE")
                else:
                    print(f"Correct answer: {correct_answer}")

    print(score)  # Output the score directly

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError("Please enter 1, 2, or 3.")
            return level
        except ValueError as ve:
            print(ve)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level specified.")

if __name__ == "__main__":
    main()
