"""

https://leetcode.com/problems/valid-parenthesis-string/

Idea:
- if star and existing open, assume )
- else, assume ""
- if hit extra ), turn ) to ""
- if hit extra ) and no ), turn "" to (

- if reach end and no neg things, all good

Alt Idea:
- consider a search alg with count of open, but notice when you branch, you are either -1, 0 or 1 change.
- So, just keep a range. When you branch it's always a continuous range. If one branch has 0, all good.

"""

def solve(s):
    hi = lo = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            hi -= 1
            lo -= 1
        else: # *
            lo -= 1
            hi += 1

        lo = max(lo, 0)
        if hi < 0:
            return False
    return lo == 0



def solve(s):
    numOpen = 0
    numStarClose = 0
    numStarEmpty = 0

    for c in s:
        if numOpen < 0:
            return False

        # will never error by opening
        if c == '(':
            numOpen += 1
        elif c == ')':
            if numOpen == 0:
                if numStarClose > 0:
                    numStarClose -= 1
                    numStarEmpty += 1
                elif numStarEmpty > 0:
                    numStarEmpty -= 1
                else:
                    return False
            else:
                numOpen -= 1
        elif c == '*':
            if numOpen > 0:
                numOpen -= 1
                numStarClose += 1
            else:
                numStarEmpty += 1

    return True if numOpen == 0 else False # catches case if on last one, it's a ( but not caught
        
