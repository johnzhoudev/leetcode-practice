"""

1768. Merge Strings Alternately

merge the letters
if one longer than other, just append letters

Time O(n)
space O(n) for the result string

Tactic:
just merge while both idx < len(str), then add tail


"""

def solve(s1, s2):
    idx = 0
    output = ""
    while idx < len(s1) and idx < len(s2):
        output += s1[idx] + s2[idx]
        idx += 1
    
    if idx < len(s1):
        output += s1[idx:]
    elif idx < len(s2):
        output += s2[idx:]
    
    return output


