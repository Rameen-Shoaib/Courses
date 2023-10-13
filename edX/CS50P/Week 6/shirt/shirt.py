import sys
from os import path
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    f = [".jpg", ".jpeg", ".png"]

    get = os.path.splitext(sys.argv[1])
    out = os.path.splitext(sys.argv[2])

    if get[1].lower() not in f:
        sys.exit("Invalid input")

    elif out[1].lower() not in f:
        sys.exit("Invalid output")

    elif get[1].lower() != out[1].lower():
        sys.exit("Input and output have different extensions")

    elif not path.exists(sys.argv[1]):
        sys.exit("File does not exist")

    else:
        shirt = Image.open("shirt.png")
        inp = Image.open(sys.argv[1])

        resize = ImageOps.fit(inp, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        resize.paste(shirt, mask=shirt)

        resize.save(sys.argv[2])