"""

14. Longest Common Prefix

just check


"""

def solve(strs):
    prefix = ""
    for idx, c in enumerate(strs[0]):
        for s in strs[1:]:
            if idx >= len(s) or s[idx] != c:
                return prefix
        
        prefix += c
    return prefix
