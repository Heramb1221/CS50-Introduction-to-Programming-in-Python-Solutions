import sys

if len(sys.argv) > 2:
    raise ValueError(sys.exit("Too many command-line arguments"))
if not sys.argv[1].endswith(".py"):
    raise ValueError(sys.exit("Not a Python file"))

numline = 0
    
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.isspace():
                continue
            if line.strip().startswith("#"):
                continue

            numline += 1
    
except FileNotFoundError:
    sys.exit("Too few command-line arguments")

print(numline)
