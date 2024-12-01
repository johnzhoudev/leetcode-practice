"""

791. Custom Sort String

order - order of chars, all unique
s = string

Permute so it's in the ordering

Order has 26 chars

just make a bucket sort type situation

O(n) time, n is s
O(n) space

"""
from collections import defaultdict

def solve(order, s):

    buckets = {}
    for c in order:
        buckets[c] = 0

    outputString = ""

    for c in s:
        if c in buckets: buckets[c] += 1
        else: outputString += c
    
    for c in order:
        outputString += c * buckets[c]
    
    return outputString


