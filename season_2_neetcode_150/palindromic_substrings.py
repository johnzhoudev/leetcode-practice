"""

https://leetcode.com/problems/palindromic-substrings/

- return number of palindromic substrings in a string

Idea:
- pali if before it is pali
- just do same middle point method

Tactic: Count palis from each middle. Remember odd and even middle.
"""

def solve(s):

    # use for s, s and s, s+1
    def countPalis(start, end):
        count = 0
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            count += 1
            start -= 1
            end += 1
        return count
    
    total = 0
    for x in range(len(s)):
        total += countPalis(x, x)
        if x+1 < len(s):
            total += countPalis(x, x+1)
    return total
        
