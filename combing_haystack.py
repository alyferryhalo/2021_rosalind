# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

import re

def combing_haystack(s, t):
    t_re = '(?=(%s))' %  re.escape(t)
    return len(re.findall(t_re, s))

s = "GATATATGCATATACTT"
t = "ATAT"

combing_haystack(s,t)
