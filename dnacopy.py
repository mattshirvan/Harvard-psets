from sys import argv, exit
import re

def main():

    # ensure proper command line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # open csv and sequence files
    csv_file = open(argv[1], "r")
    sequence_file = open(argv[2], "r")

    # read contents into memory
    csv = csv_file.read()
    sequence = sequence_file.read()

    # for each str count repetition
    agat = re.search("AGATC", sequence)
    aatg = re.search("AATG", sequence)
    tatc = re.search("TATC", sequence)
    ttct = re.search("TTTTTTCT", sequence)
    tctag = re.search("TCTAG", sequence)
    gata = re.search("GATA", sequence)
    gaaa = re.search("GAAA", sequence)
    tctg = re.search("TCTG", sequence)

    # small sequence
    # compare the str count against
    # if agat and aatg and tatc:
    #     agat_count = sequence.count(agat.group())
    #     aatg_count = sequence.count(aatg.group())
    #     tatc_count = sequence.count(tatc.group())

    #     # AGATC AATG TATC
    #     name = re.search(f"{agat_count},{aatg_count},{tatc_count}", csv_file.read())
    #     if name:
    #         found = name.string.splitlines()
    #         index = [i for i, val in enumerate(found) if name.group() in val]
    #         dna = found[index[0]].split(",")
    #         print(dna[0])
    #     else:
    #         print("No match")
    #         exit(1)

    # # no matches at all
    # else:
    #     print("No match")
    #     exit(1)

    # large sequence
    # compare the str count against
    if agat and ttct and aatg and tctag and gata and tatc and gaaa and tctg:
        agat_count = sequence.count(agat.group())
        ttct_count = sequence.count(ttct.group())
        aatg_count = sequence.count(aatg.group())
        tctag_count = sequence.count(tctag.group())
        gata_count = sequence.count(gata.group())
        tatc_count = sequence.count(tatc.group())
        gaaa_count = sequence.count(gaaa.group())
        tctg_count = sequence.count(tctg.group())

        # AGATC TTTTTTCT AATG TCTAG GATA TATC GAAA TCTG
        name = re.search(f"{agat_count},{ttct_count},{aatg_count},{tctag_count},{gata_count},{tatc_count},{gaaa_count},{tctg_count}", csv)
        print(name)
        print(f"{agat_count},{ttct_count},{aatg_count},{tctag_count},{gata_count},{tatc_count},{gaaa_count},{tctg_count}")
        if name:
            found = name.string.splitlines()
            index = [i for i, val in enumerate(found) if name.group() in val]
            dna = found[index[0]].split(",")
            print(dna[0])
        else:
            print("No match")
            exit(1)

    # no matches found
    else:
        print("No match")
        exit(1)
main()