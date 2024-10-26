def main():
    p = input("Input: ")
    print(shorten(p))

def shorten(word):
    def shorten(word):
    vowels = "aeiou"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
