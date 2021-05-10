# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair 
# and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset: 5 3
# Sample Output: 19

def fibborabbits(months, offsprings):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child

n = int(input())
k = int(input())

fibborabbits(n, k)
