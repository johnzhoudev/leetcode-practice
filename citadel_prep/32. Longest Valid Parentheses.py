"""

32. Longest Valid Parentheses

invalid if open and no closed at end - expand until good
    - preprocess, count number of unmatched closed brackets towards end.

or closed and no open before it - skip and restart window

O(n)

Better: 
Use stack and push open brackets. 

tactic:
Stack, push indices of open brackets and closed brackets. Then, stack will contain invalid points. inbetween + start / end will give valid regions.

"""

def solve(s):
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif stack and s[stack[-1]] == '(':
            stack.pop()
        else:
            stack.append(i)
    
    # Now find inbetweens.
    best = 0
    stack = [-1] + stack + [len(s)] # fancy trick!
    for i in range(len(stack) - 1):
        j = i + 1

        best = max(best, stack[j] - stack[i] - 1)
    return best






def solve(s):
    closed = 0
    counts = [0 for i in range(len(s))]
    for i in range(len(s) -1, -1, -1):
        if s[i] == ')':
            closed += 1
        else:
            closed = max(0, closed - 1) # either restart count, or continue
        counts[i] = closed

    # Now go forward
    bestLen = 0
    currLen = 0
    openCount = 0
    # print(counts)
    for i, c in enumerate(s):
        # print(openCount, currLen, bestLen)
        if c == ')':
            if openCount == 0: # fail
                # reset, don't take
                currLen = 0
                openCount = 0
                continue
            else:
                openCount -= 1
        elif c == '(':
            openCount += 1
            if i+1 >= len(counts) or counts[i+1] < openCount: # are there enough closing brackets to continue?
                # skip
                currLen = 0
                openCount = 0
                continue
        
        currLen += 1 # add current
        bestLen = max(bestLen, currLen)
    
    return bestLen



print(solve("(()"))