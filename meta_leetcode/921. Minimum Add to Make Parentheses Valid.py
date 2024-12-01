"""

921. Minimum Add to Make Parentheses Valid

empty
AB concat, valid
(A) is valid

can insert at any position

Count the number of non-paired parentheses and add them?
- closed parenthese with no open ones
- open ones at end with no closed

go thru with open parentheses count, and count invalid

Tactic:
Just count number of bad parentheses.

"""

def solve(s):
    openCount = 0
    badCount = 0

    for c in s:
        if c == '(':
            openCount += 1
        elif c == ')':
            if openCount == 0:
                badCount += 1
            else:
                openCount -= 1
    
    return badCount + openCount




