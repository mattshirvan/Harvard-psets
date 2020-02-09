from sys import argv, exit
import re
import difflib

def main():

    # ensure proper command line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # open csv and sequence files
    csv_file = open(argv[1], "r")
    sequence_file = open(argv[2], "r")

    # read contents into memory
    # csv = csv_file.read()
    sequence = sequence_file.read()

    # for each str count repetition
    agat = re.findall("AGATC(?=AGATC)", sequence)
    ttct = re.findall("TTTTTTTC(?<=TTTTTTTC)", sequence)
    aatg = re.findall("AATG(?=AATG)", sequence)
    tctag = re.findall("TCTAG(?=TCTAG)", sequence)
    gata = re.findall("GATA(?=GATA)", sequence)
    tatc = re.findall("TATC(?=TATC)", sequence)
    gaaa = re.findall("GAAA(?=GAAA)", sequence)
    tctg = re.findall("TCTG(?=TCTG)", sequence)


    # AGATC,TTTTTTTC,AATG,TCTAG,GATA,TATC,GAAA,TCTG
    dna = f"{len(agat)+1},{len(ttct)+1},{len(aatg)+1},{len(tctag)+1},{len(gata)+1},{len(tatc)+1},{len(gaaa)+1},{len(tctg)+1}"
    result = difflib.get_close_matches(dna , csv_file.readlines(), 1, 0)[0]
    name = result.split(',')
    print(name[0])
main()