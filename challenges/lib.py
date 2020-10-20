complements = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A'
}

codon_table_raw = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''

items = codon_table_raw.split()
codons = items[::2]
proteins = items[1::2]
codon_table = dict(zip(codons, proteins))

def complement(seq):        
    return ''.join([complements[c] for c in seq])

def reverse_complement(seq):
    return complement(seq[::-1])

def transcribe(dna):
    rna = dna.replace('T', 'U')
    return rna

def translate(rna):
    assert (len(rna) % 3 == 0)
    protein = [codon_table[rna[ptr:ptr+3]] for ptr in range(0, len(rna), 3)]
    return ''.join([p if p != 'Stop' else '' for p in protein])

def substring(source, substring):
    locations = []
    for i in range(0, len(source) - len(substring)):
        if source[i:i+len(substring)] == substring:
            locations.append(i+1) # 1 indexed
    return locations

assert 'TACG' == complement('ATGC')
assert 'GCAT' == reverse_complement('ATGC')