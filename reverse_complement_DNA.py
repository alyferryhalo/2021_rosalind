# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string is the string sc formed by reversing the symbols, 
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string of length at most 1000 bp.
# Return: The reverse complement

# Sample Input AAAACCCGGT
# Sample Output ACCGGGTTTT

# AT; GC

DNA_seq = 'AAAACCCGGT'

DNA_reverse_complement = []

def reverse_complement_DNA(DNA_seq):
    DNA_reverse = DNA_seq[::-1]
    for nuc in DNA_reverse:
        if nuc == "A":
            DNA_reverse_complement.append("T")
        elif nuc == "T":
            DNA_reverse_complement.append("A")
        elif nuc == "G":
            DNA_reverse_complement.append("C")
        elif nuc == "C":
            DNA_reverse_complement.append("G")
    print(DNA_reverse_complement)

reverse_complement_DNA(DNA_seq)
