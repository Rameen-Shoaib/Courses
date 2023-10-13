import sys
from os import path

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")
else:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        whitespace = 0
        comments = 0
        count = 0

        for line in lines:
            line = line.strip().split('\n')
            for c in line:
                if len(c) < 1 and c.isalnum() == False:
                    whitespace += 1
                elif c.startswith('#'):
                    comments += 1
                else:
                    count += 1

        print(count)