def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 0  

if __name__ == "__main__":
    main()
