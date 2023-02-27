# Results:
# Runtime: 27ms 97.19%
# Memory Usage: 14.1MB 97.28%

"""

https://leetcode.com/problems/generate-parentheses/

generate all combos of parentheses, given n

Idea:
- To generate, you can either open a new parentheses or close an existing one, if it exists
- maintain count of open parentheses, and total paren? then do search alg?

Tactic: Backtracking alg, either open a new paren or close existing one. Track numOpen/numClosed, or numLeft/numRight brackets

"""

def solve(n):
    # setup state
    state = [("", 0, 0)] # (str, num open paren, total closed paren)
    results = []

    while len(state) != 0:
        s, numOpen, numClosed = state.pop()

        # case 0, finished. add to results
        if numOpen == 0 and numClosed == n:
            results.append(s)
            continue

        # case 1, open a new one
        if numOpen + numClosed < n:
            state.append((s + "(", numOpen + 1, numClosed))
        
        # case 2, close one
        if numOpen != 0:
            state.append((s + ")", numOpen - 1, numClosed + 1))
    
    return results



