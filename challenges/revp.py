from Bio import SeqIO

complements = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A'
}

def complement(seq):        
    return ''.join([complements[c] for c in seq])

def reverse_complement(seq):
    return complement(seq[::-1])

def find_restriction_sites(seq):
    restriction_sites = []
    for i in range(len(seq)):
        for j in range(4,13,2):
            if i + j > len(seq):
                break
            substr = seq[i:i+j]
            if reverse_complement(substr) == substr:
                restriction_sites.append((i+1,j))
    return restriction_sites


assert 'TACG' == complement('ATGC')
assert 'GCAT' == reverse_complement('ATGC')

if __name__ == "__main__":
    restriction_sites = []

    with open("challenges/files/rosalind_revp.fasta", "rU") as fp:
        for record in SeqIO.parse(fp, "fasta"):
            restriction_sites = find_restriction_sites(record.seq)
    
    for i,j in restriction_sites:
        print(i, j)
