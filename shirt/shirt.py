import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        print("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not (input_path.lower().endswith(valid_extensions) and output_path.lower().endswith(valid_extensions)):
        print("Invalid output")
        sys.exit(1)

    if os.path.splitext(input_path)[1].lower() != os.path.splitext(output_path)[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.exists(input_path):
        print("Input does not exist")
        sys.exit(1)

    try:
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")
        input_image = ImageOps.fit(input_image, shirt_image.size)
        input_image.paste(shirt_image, shirt_image)
        input_image.save(output_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
