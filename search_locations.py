# The location of a substring s[j:k] is its beginning position j; note that t
# will have multiple locations in s if it occurs more than once as a substring of s.

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

def search_locations(s,t):
    matches = []
    i = 0
    while i > -1:
        i = s.find(t,i)
        if i > -1:
            si += 1
            matches.append(i)
    return matches

s = "GATATATGCATATACTT"
t = "ATAT"

search_locations(s,t)
