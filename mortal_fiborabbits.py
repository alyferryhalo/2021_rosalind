# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, 
# which followed the recurrence relation Fn=Fn−1+Fn−2
# and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution 
# in the case that all rabbits die out after a fixed number of months. 

# Given: Positive integers n≤100 and m≤20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

def mortal_fiborabbits(n,m):
    def help_func(p):
        return [sum([p[i] for i in range(1,len(p))])] +\ [p[i] for i in range(0,len(p)-1)]
        
    result = [1]
    while len(result) < m:
        result.append(0)
    for i in range(n-1):
        result = help_func(result)
    return sum(result)

n = 6 
m = 3

mortal_fiborabbits(n,m)
