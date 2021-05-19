# DNA Strings
#	A T C C A G C T
#	G G G C A A C T
#	A T G G A T C T
#	A A G C A A C C
#	T T G G A A C T
#	A T G C C A T T
#	A T G G C A C T

# Profile
#A   5 1 0 0 5 5 0 0
#C   0 0 1 4 2 0 6 1
#G   1 1 6 3 0 1 0 0
#T   1 5 0 0 0 1 1 6

# Consensus
# A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length in FASTA format.

# Return: A consensus string and profile matrix for the collection.

def create_matrix(matrix):
    with open("DNA_matrix.fasta", "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                seq = next(file).strip()
                matrix.append(seq)
    return matrix

def create_profile(matrix):
    pass

def create_consensus(matrix):
    pass

matrix = []
create_matrix(matrix)

print("DNA Strings:")
print('\n'.join(matrix))
print("===============")
print("Profile:")
print("===============")
print("Consensus:")
