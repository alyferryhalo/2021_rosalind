# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string
# corresponding to a coding strand, its transcribed RNA string is formed by replacing all occurrences of 'T' in t with 'U'

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t

DNA_seq = "GATGGAACTTGACTACGTAAATT"

def DNA_RNA_convert(DNA_seq):
  RNA_seq = DNA_seq.replace('T', 'U')
  print(RNA_seq)

DNA_RNA_convert(DNA_seq)

# GAUGGAACUUGACUACGUAAAUU
