from sys import argv, exit
import cs50
import csv

# ensure correct command line arguments
if len(argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(0)

# create connection to database
db = cs50.SQL("sqlite:///students.db")

# read the csv into memory and
# create an instance of dictionary
with open(argv[1], "r") as file:
    csv_file = csv.DictReader(file)

    # read rows in csv file
    for row in csv_file:

        # check if the row is name
        name = row["name"].split()

        # check length of name list
        if len(name) == 3:
            first = name[0]
            middle = name[1]
            last = name[2]
        elif len(name) == 2:
            first = name[0]
            middle = None
            last = name[1]

        # set house and birth
        house = row["house"]
        birth = row["birth"]

        # print(first, middle, last,  house, birth)
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)



