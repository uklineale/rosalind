from Bio import SeqIO
from lib import complement, substring, translate, transcribe
import sys

def splice_rna(dna, introns):
    for i in introns:
        dna = dna.replace(i, '')

    rna = transcribe(dna)
    return translate(rna)

if __name__ == "__main__":
    input_file = ''
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "challenges/files/splc.fasta"
    print("Reading from file: " + input_file)
    with open(input_file, "rU") as fp:
        i = 0
        dna = ''
        introns = []

        for record in SeqIO.parse(fp, "fasta"):
            if i == 0:
                dna = str(record.seq)
            else:
                introns.append(str(record.seq))
            
            i += 1
        
        print(splice_rna(dna, introns))