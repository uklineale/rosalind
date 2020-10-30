from Bio import SeqIO
from lib import bases

def profile_matrix(strings):
    profile = {k:[] for k in bases}
    for s in strings:
        for c in s:
            profile[c] += 1
    return profile

if __name__ == "__main__":
    input_file = ''
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "challenges/files/cons.fasta"

    strings = []
    with open(input_file, "rU") as fp:
        for record in SeqIO.parse(fp, "fasta"):
            strings.append(str(record.seq))
    
    print(strings)