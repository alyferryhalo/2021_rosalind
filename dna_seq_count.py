# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
# the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string
# of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T'

dna_seq = 'ACTTACTAGCGCAAGGTGAGTAAGACCGGACCCTACTGATATATTCATACGCCCCACGCCGTCGATGCACACACGTACATAGGTGTCAAGATCGCTTTATCCAGCTGTCCTCCGTACATAGACTCACCTAACCCCGCGGCGACTCACGTGCGTATATTTAGACCGGACACTGATAAGAGCCGATATAACACTTCAGATTCACTAAACTGTGACTGGAGCGACGTCAGCTTGGGTCCCGCAGTTATACAATTACATAGGTAGCGGTGGCTTTCGGATTTCAATTTATGTGCGATCGTCACGAAAACGCTTCTTCGAGAAGGCTCTTCGACGGTAGGGAGGCGACGTGCTCAGGACCAGTCCTTAGACTATCAAACCCAAAACTAGCATATTGTGGCGCAGATGATCGATAAATTCTACTCAGCTGCAGAAGAATTCGCAGGTGAATAGAGTTAAAGGTACACACGCGTGGTTGAACCAAACAAACTATTATCCGCCTTTGGTGTATCCCGAGAGTTGCCCCGGCGAAGCCAGTTGACGAAGGTTCTTAAAAAGTGCAAGTCCTTCCGGTGCGCCACATGTAAAAGACCTTTATGGCCATATGTAGTACTACAGCATGGTGGATTAAAATTCCAATAATCTACCGGTGGTCCCCGCCCATGGTGCCCCCTGGAAGAGGAGAGGGGCTCTAAGGGAGTGAAAAATCTAGTTGAGTAAGTGGGCCACGGGCAATTAACATGCGCTGGTGCTTAGAACACCGGTGCCAACTTCATCAGATTTTCATCTACTGTTCTCCAGCCGTCGGCCTCTGGCTTCGACAGCGGCCCAGGAAATGCGTACATATGCCTTGAACATCATAACGTACTATAAGCTTGCGGTTGGCCTGGGCCCTCGCAGTTTCGGGCTTGGCGGAACGGTCTAGCTATTTTTGGCGCCCACATACCTGCTGGAG'

def count_ATGC(dna_seq):
  A = dna_seq.count('A')
  T = dna_seq.count('T')
  G = dna_seq.count('G')
  C = dna_seq.count('C')
  print(f"{A} {T} {G} {C}")

count_ATGC(dna_seq)