"""

131. Palindrome Partitioning

all possible partitions of palindromes

Start with individual letters - all palindromes
- then, either join same letters one after the other, OR join 2 different
    - to avoid dupes, only join 1 letter at a time
- so it's either join same letter once, or join 2 that are diff.

aa b a b aa

- search alg for each case
    - dfs, for each elt in the string, see if you can join

"""

def solve(s):
