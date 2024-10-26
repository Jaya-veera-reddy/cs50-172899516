

import sys
import random
import pyfiglet

def main():

    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")


    font = None


    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        font = sys.argv[2]


    if font is None:
        fonts = pyfiglet.FigletFont.getFonts()
        font = random.choice(fonts)


    if font not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")


    user_input = input("Input: ")


    figlet = pyfiglet.Figlet(font=font)

    
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
