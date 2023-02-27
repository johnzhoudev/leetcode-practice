"""

https://leetcode.com/problems/valid-parentheses/description/

Idea: Use stack

Tactic: Stack. Caution, don't forget about if stack empty or at end, still stuff in stack edge cases

"""

def solve(s):
    stack = []
    bMap = { '(':')', '{':'}', '[':']'}
    openB = "({["

    for b in s:
        if b in openB:
            stack += [b]
        else:
            if len(stack) == 0 or bMap[stack.pop()] != b:
                return False
    
    return len(stack) == 0
            

