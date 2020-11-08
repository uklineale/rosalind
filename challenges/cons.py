from Bio import SeqIO
from lib import get_profile, get_consensus_string, arg_path_or_default

def print_profile(profile):
    for k, v in profile.items():
        print(k + ": ", end='')
        for count in v:
            print(str(count) + " ", end='')
        print("") #

if __name__ == "__main__":
    input_file = arg_path_or_default("challenges/files/cons.fasta")
    with open(input_file, "rU") as fp:
        strings = []
        for record in SeqIO.parse(fp, "fasta"):
            strings.append(str(record.seq))
        profile = get_profile(strings)
        print(get_consensus_string(profile))
        print_profile(profile)