import sys
import csv
from tabulate import tabulate
from os import path

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")
else:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file, delimiter=',')
        headers = next(reader)

        tables = []
        for row in reader:
            tables.append(row)

        print(tabulate(tables, headers, tablefmt="grid"))