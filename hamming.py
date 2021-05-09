s_seq = "GAGCCTACTAACGGGAT"
t_seq = "CATCGTAATGACGGCCT"

def hamming(s_seq,t_seq):
    result=0
    for x,(i,j) in enumerate(zip(s_seq,t_seq)):
        if i!=j:
            result+=1
    return result

print(hamming(s_seq,t_seq))
