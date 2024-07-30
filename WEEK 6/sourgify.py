import sys
import csv

if len(sys.argv) > 3:
    raise ValueError(sys.exit("Too many command-line arguments"))
if len(sys.argv) < 3:
    raise ValueError(sys.exit("Too many command-line arguments"))

students = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last , first = row["name"].split(", ")
            house = row["house"]

            students.append({"first": first, "last": last, "house": house})

    with open(sys.argv[2], "a") as file:
        for student in students:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})

except FileNotFoundError:
    sys.exit("File does no exist")
