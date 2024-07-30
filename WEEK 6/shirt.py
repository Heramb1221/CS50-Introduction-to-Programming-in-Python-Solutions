from PIL import Image, ImageOps
import sys
import os

if len(sys.argv) > 3:
    raise ValueError(sys.exit("Too few command-line arguments"))
if len(sys.argv) < 3:
    raise ValueError(sys.exit("Too many command-line arguments"))

try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as input:
        input_cropped = ImageOps.fit(input, shirt.size)
        input_cropped.paste(shirt, mask = shirt)
        input_cropped.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
