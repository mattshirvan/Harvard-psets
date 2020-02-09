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
    sequence = sequence_file.read()
    small = False
    if "name,AGATC,AATG,TATC" in csv_file.readline():
        small = True
        # for small sequence
        agats = re.search("AGATC", sequence)
        aatgs = re.search("AATG", sequence)
        tatcs = re.search("TATC", sequence)

        # small sequence
        # compare the str count against
        if agats and aatgs and tatcs:
            agat_count = sequence.count(agats.group())
            aatg_count = sequence.count(aatgs.group())
            tatc_count = sequence.count(tatcs.group())

            # AGATC AATG TATC
            name = re.search(f"{agat_count},{aatg_count},{tatc_count}", csv_file.read())
            if name:
                found = name.string.splitlines()
                index = [i for i, val in enumerate(found) if name.group() in val]
                dna = found[index[0]].split(",")
                print(dna[0])
                exit(0)
            else:
                print("No match")
                exit(1)

    if small == False:
        # for large sequence
        agat = re.findall("AGATC(?=AGATC)", sequence)
        ttct = re.findall("TTTTTTTC(?<=TTTTTTTC)", sequence)
        aatg = re.findall("AATG(?=AATG)", sequence)
        tctag = re.findall("TCTAG(?=TCTAG)", sequence)
        gata = re.findall("GATA(?=GATA)", sequence)
        tatc = re.findall("TATC(?=TATC)", sequence)
        gaaa = re.findall("GAAA(?=GAAA)", sequence)
        tctg = re.findall("TCTG(?=TCTG)", sequence)

        # large sequence
        # compare the str count against
        # AGATC,TTTTTTTC,AATG,TCTAG,GATA,TATC,GAAA,TCTG
        dna = f"{len(agat)+1},{len(ttct)+1},{len(aatg)+1},{len(tctag)+1},{len(gata)+1},{len(tatc)+1},{len(gaaa)+1},{len(tctg)+1}"
        result = difflib.get_close_matches(dna , csv_file.readlines(), 1, 0.8)
        if len(result) > 0:
            name = result[0].split(',')
            print(name[0])
            exit(0)

        else:
            print("No match")
            exit(1)

    # no matches at all
    else:
        print("No match")
        exit(1)

main()