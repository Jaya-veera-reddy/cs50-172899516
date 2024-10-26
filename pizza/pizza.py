import sys
import os
import csv
from tabulate import tabulate

def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            rows = [row for row in reader]
        return headers, rows
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print("File does not exist")
        sys.exit(1)

    headers, rows = read_csv(file_path)
    print(tabulate(rows, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
