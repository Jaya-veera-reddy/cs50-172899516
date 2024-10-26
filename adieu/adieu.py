import sys

def main():
    names = []

    try:
        while True:
            name = input().strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    if not names:
        print("Please provide at least one name.")
        sys.exit(1)

    farewell_message = "Adieu, adieu, to "

    if len(names) == 1:
        farewell_message += names[0]
    elif len(names) == 2:
        farewell_message += f"{names[0]} and {names[1]}"
    else:
        farewell_message += ", ".join(names[:-1]) + f", and {names[-1]}"

    print(farewell_message)

if __name__ == "__main__":
    main()
