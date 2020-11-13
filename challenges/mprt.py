import requests
from Bio import SeqIO
from lib import get_protein_motif_locations

base_url = "http://www.uniprot.org/uniprot/"
filename = "challenges/files/mprt.fasta"
test_proteins = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
actual_proteins = ['P05113_IL5_HUMAN', 'P08318_P100_HCMVA', 'P01044_KNH1_BOVIN', 'Q03745', 'A5GVY9', 'B3PYU7', 'P36913_EBA3_FLAME', 'P10643_CO7_HUMAN', 'P40225_TPO_HUMAN', 'P02748_CO9_HUMAN', 'P01189_COLI_HUMAN', 'A6UDH9', 'A3N0C7', 'B5FNU0', 'Q5U1Y9']
test_protein = "sp|B5ZC00|SYG_UREU1"
n_glycosylation_motif = "N{P}[ST]{P}"

def load_proteins(ids):
    with open(filename, "w") as fp:
        for uniprot_id in ids:
            print("starting %s" % uniprot_id)
            response = requests.get(base_url + uniprot_id + ".fasta")
            fp.write(response.text)

if __name__ == "__main__":
    protein_ids = actual_proteins
    # protein_ids = test_proteins
    load_proteins(protein_ids)
    with open(filename, "rU") as fp:
        i = 0 # counter to associate protein_id with matches
        for record in SeqIO.parse(fp, "fasta"):
            locations = get_protein_motif_locations(str(record.seq), n_glycosylation_motif)
            if len(locations) > 0:
                print(protein_ids[i])
                print(*locations)
            i += 1
