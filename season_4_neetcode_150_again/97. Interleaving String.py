"""

97. Interleaving String

- greedy? just take when you can?
- or stack? keep going and pop when you can't => dfs

Brute force:
- search alg, try all combos of choices - O(2^n)
    - could be repeated work, so could memoize
    dfs(idx s1, idx s2) to be used
        - idx s3 is s1 + s2

- more creative? pretty much have to check all possibilities. How to know which one is right? not trivial
O(nm)

Tactic:
dfs(idx1, idx2) with memoization. Pretty much have to check all possibilities => make efficient with memo

"""

def solve(s1, s2, s3):
    # early return
    if len(s3) != len(s1) + len(s2): return False

    cache = {}

    def dfs(idx1, idx2):
        idx3 = idx1 + idx2

        # done conditions
        if idx3 == len(s3): return True

        # check cache
        if (idx1, idx2) in cache: return cache[(idx1, idx2)]

        # do work
        # choose to use either right or left
        if idx1 < len(s1) and s1[idx1] == s3[idx3]:
            if dfs(idx1 + 1, idx2): return True
        
        if idx2 < len(s2) and s2[idx2] == s3[idx3]:
            if dfs(idx1, idx2 + 1): return True
        
        # if we find a true, we just break all
        # only store falses in cache
        cache[(idx1, idx2)] = False
        return False
    
    return dfs(0, 0)
            






