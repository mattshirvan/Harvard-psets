from sys import argv, exit
import cs50

# ensure correct command line arguments
if len(argv) != 2:
    print("Usage: python roster.py Gryffindor")
    exit(0)

# open the database
db = cs50.SQL("sqlite:///students.db")

# set house from command line
house = argv[1]

# query the database for student roster
roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last", house)

# print house roster
for row in roster:
    if row["middle"] != None:
        print(row["first"], row["middle"], row["last"] + ", born", row["birth"])
    print(row["first"], row["last"] + ", born", row["birth"])
