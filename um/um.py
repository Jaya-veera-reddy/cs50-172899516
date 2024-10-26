import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use a regex pattern to match the word "um" case-insensitively
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
