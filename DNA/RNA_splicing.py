# Dictionary for RNA codons and their amino acids
RNA_codons = {
    # 'M' - START, '' - STOP
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

# Opening and reading the file given by rosalind containing a fasta file
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
file = open("/Users/macbook/python/rosalind/test_data/RNA_splicing.txt", "r")

# Creating a list of strings, each string corresponding to a line in the file
strings = file.readlines()

# Removing \n from the end of each line
new_strings = [line.strip() for line in strings]

# Assigning the second line as the DNA sequence of interest
DNA_seq = new_strings[1]

# Creating empty list for introns
introns = []

# Looping through values in strings with odd index number, adding them to list of introns
[introns.append(new_strings[i]) for i in range(len(new_strings)) if i > 2 and i%2 != 0]

# Function which loops through each section of DNA sequence checking if it matches the intron and if so, removes it
def remove_introns(DNA_seq, intron):
    n, m = len(DNA_seq), len(intron)
    for i in range (n):
        if DNA_seq[i:i+m] == intron:
            DNA_seq =  DNA_seq[:i] + DNA_seq[i+m:]
    return DNA_seq

# Function which transcribes DNA into RNA
RNA_seq = ""
def transcription(DNA_seq, RNA_seq):
    for nt in DNA_seq:
        if nt == "T":
            RNA_seq += "U"
        else:
            RNA_seq += nt
    return RNA_seq

protein = ""
def translation(RNA_codons, RNA_seq, protein):
    init_pos = 0
    for pos in range(init_pos, len(RNA_seq) - 2, 3):
        protein += RNA_codons[RNA_seq[pos:pos + 3]]
    return protein

# Loops through each intron and uses remove_introns function
for intron in introns:
    DNA_seq = remove_introns(DNA_seq, intron)

# Uses transcription function
RNA_seq = transcription(DNA_seq, RNA_seq)

print(translation(RNA_codons, RNA_seq, protein))