import sys
import os

def count_lines_of_code(file_path):
    loc = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    loc += 1
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return loc

def main():
    if len(sys.argv) != 2:
        print("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print("File does not exist")
        sys.exit(1)

    loc = count_lines_of_code(file_path)
    print(loc)

if __name__ == "__main__":
    main()
