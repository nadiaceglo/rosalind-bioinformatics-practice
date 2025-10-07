RNA_codons = {
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "", "UAG": "", "UGA": ""
}

def transcription(seq):
    return seq.replace("T", "U")

def reverse_complement(seq):
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def translation(seq, RNA_codons):
    proteins = set()
    for frame in range(3):
        rna = seq[frame:]
        for i in range(0, len(rna) - 2, 3):
            codon = rna[i:i+3]
            if codon == "AUG":  # Start codon
                protein = ""
                for j in range(i, len(rna) - 2, 3):
                    aa = RNA_codons.get(rna[j:j+3], "")
                    if aa == "":  # Stop codon
                        proteins.add(protein)
                        break
                    protein += aa
    return proteins

# Read FASTA file
# Given: A DNA string s of length at most 1 kbp in FASTA format.
with open("/Users/macbook/python/rosalind/test_data/open_reading_frames.txt", "r") as f:
    seq = "".join(line.strip() for line in f if not line.startswith(">"))

# Transcribe both strands
rna_seq = transcription(seq)
rev_rna_seq = transcription(reverse_complement(seq))

# Translate all 6 frames
orfs = translation(rna_seq, RNA_codons) | translation(rev_rna_seq, RNA_codons)

# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
for protein in orfs:
    print(protein)
