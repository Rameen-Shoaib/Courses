import random
import sys
from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv) == 1:
    text = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(text))
    sys.exit()

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                text = input("Input: ")
                f = sys.argv[2]
                figlet.setFont(font=f)
                print(figlet.renderText(text))
                sys.exit()

            else:
                sys.exit("Invalid Usage")

    else:
         sys.exit("Invalid Usage")

else:
     sys.exit("Invalid Usage")
