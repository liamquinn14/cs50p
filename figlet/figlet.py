from pyfiglet import Figlet # type: ignore
from pyfiglet import FigletFont # type: ignore
import random
import sys

fonts_list = FigletFont.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts_list:
            selected_font = sys.argv[2]
            f = Figlet(font=selected_font)
            user_text = input("Input: ")
            sys.exit(f.renderText(user_text))
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
elif len(sys.argv) == 1:
    selected_font = random.choice(fonts_list)
    f = Figlet(font=selected_font)
    user_text = input("Input: ")
    sys.exit(f.renderText(user_text))
else: 
    sys.exit("Invalid Usage")