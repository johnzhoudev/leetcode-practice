"""

https://leetcode.com/problems/palindrome-partitioning/

- Every substring is a palindrome (same fwd / back)
    - must all be same letter: if 2 different letters, those are start and end of substr.

- return all possible partitionings.

- Starting point, all letters separate
    - on each backtrack, join regions if same letter
    - try joining adjacent lists if all have same letter
        - use copies, so can do iterative. no easy way to "pop" the state

Incorrect:
- every substring of partition must be palindrome - but doesn't mean all substrings


Idea 2:
- Or build palindrome by joining 2 of same letters - even palindrome
- need to build palindrome from middle, but should be possible to still keep unique.
    - to build, join with adjacent ones on both sides
    - Or, with one that has the same letter


To build palindromes
    - either add 1 letter at a time from both sides
    - Or, if single char, add one to the left.
    - This is a unique way of building a palindrome that we can backtrack on.

"""

def solve(s):
    state = [c for c in s]
    solns = []

    def backtrack(state, i):
        solns.append(state) # can just append, no need to copy

        # pick next index to start modifying
        for k in range(i, len(state)):

            # case 1, if one letter, can append to next if fine
            if len(state[k]) == 1 and k + 1 < len(state) and state[k+1] == state[k]:
                end = [] if k+2 == len(state) else state[k+2:]
                backtrack(state[:k] + [state[k] + state[k+1]] + end, k)
            
            # case 2, try expanding sideways
            if k-1 >= 0 and k+1 < len(state) and len(state[k-1]) == 1 and len(state[k+1]) == 1 and state[k-1] == state[k+1]:
                end = [] if k+2 == len(state) else state[k+2:]
                backtrack(state[:k-1] + [state[k-1] + state[k] + state[k+1]] + end, k-1)

    backtrack(state, 0)

    return solns




def solve(s):

    # first separate all strings
    state = [c for c in s]
    solns = []

    # now backtrack and try and combine, only combine forward

    def backtrack(state, i):
        # passing in a copy of state, so can just append.
        solns.append(state)

        # now try and append going forward
        for k in range(i, len(state)):
            if k + 1 == len(state) or state[k][0] != state[k+1][0]:
                continue
            
            # otherwise can be combined, so combine and backtrack
            stateCopy = state.copy()
            stateCopy[k] += stateCopy[k+1]
            del stateCopy[k+1]
            backtrack(stateCopy, k)
    
    backtrack(state, 0)

    return solns

            



