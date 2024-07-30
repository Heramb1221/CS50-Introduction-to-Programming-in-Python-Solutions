import sys
import tabulate
import csv

if len(sys.argv) > 2:
    raise ValueError(sys.exit("Too many command-line arguments"))
if not sys.argv[1].endswith(".csv"):
    raise ValueError(sys.exit("Not a CSV file"))

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        table = []
        headers = list(next(reader))
        for line in reader:
            table.append([line[0] , line[1] , line[2]])
        print(tabulate.tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("Too few command-line arguments")
