# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing 
# a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def mendelian_inheritance(k, m, n):
    T = k + m + n
    Z = T*(T - 1)
    return round(1-(n*(n-1) + 0.25*m*(m-1) + m*n)/Z, 5)

k = 2
m = 2
n = 2

mendelian_inheritance(k, m, n)
