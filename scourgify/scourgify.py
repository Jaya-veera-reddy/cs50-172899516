import sys
import csv
import os

def scourgify(input_file, output_file):
    try:
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)
            rows = []
            for row in reader:
                if 'name' in row and 'house' in row:
                    last, first = row['name'].split(', ')
                    rows.append({'first': first, 'last': last, 'house': row['house']})
                else:
                    print(f"Invalid format in {input_file}")
                    sys.exit(1)
    except FileNotFoundError:
        print(f"Could not read {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    try:
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        print(f"Could not write to {output_file}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.csv'):
        print(f"Invalid format: {input_file}")
        sys.exit(1)

    scourgify(input_file, output_file)

if __name__ == "__main__":
    main()
