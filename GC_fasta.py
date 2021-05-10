# The GC-content of a DNA string is given by the percentage of symbols in the string 
# that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. 

# DNA strings must be labeled when they are consolidated into a database. 
# A commonly used method of string labeling is called FASTA format.
# In this format, the string is introduced by a line that begins with '>', 
# followed by some labeling information.

# In Rosalind's implementation, a string in FASTA format will be labeled 
# by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 

# Sample Dataset: check GC_content.fasta
# Sample Output: Rosalind_0808 \n 60.919540


from operator import itemgetter

def GC_fasta(results):
	with open("GC_content.fasta", "r") as file:
		for line in file:
			line = line.strip()
				if line[0] in ">":
					header = line[1:]
					seq = next(file).strip()
					gc = sum(1 for base in seq if base.lower() in "gc")
					results.append((header, gc / len(seq) * 100))
	return results

results = []
result = max(results, key=itemgetter(1))
print("{}\n{:.6f}".format(*result))
