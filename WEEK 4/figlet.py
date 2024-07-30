import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(list)
    figlet.setFont(font=f)
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font = sys.argv[2]
        if font not in list:
            exit("Invalid usage")
        figlet.setFont(font=font)
    else:
        exit("Invalid usage")
else:
    exit("Invalid usage")

fg = input("Input: ")
print(figlet.renderText(fg))
