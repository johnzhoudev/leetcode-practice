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

Alt: Backtrack, either take the current string and see if it's a palindrome, or continue.
- track index in s we're at
- some weird caching of isPalindrome. Depending on how you search, if you check smaller results first, you will
    have checked the inner text. so can determine if palindrome in O(1) if check inside, and letters are same

Tactic: Backtrack by either choosing next palindrome (and checking isPalindrome with DP) or building palindromes by merging letters uniquely, either add 1 letter to both sides or if single letter, matching to right

"""

def solveAlt(s):
    cache = {}
    def isPalindromeSlow(left, right):
        nonlocal cache
        if (left, right) in cache:
            return cache[(left, right)]
        string = s[left:right+1]
        isPal = string[::-1] == string
        if isPal:
            while left <= right:
                cache[(left, right)] = True
                left += 1
                right -= 1
        return isPal
    
    def isPalindrome(left, right):
        nonlocal cache
        isPal = False
        if (left, right) in cache:
            return cache[(left, right)]
        elif (((left + 1, right - 1) in cache and cache[(left+1, right-1)]) or (right - left + 1 <= 2)) and s[left] == s[right]:
            cache[(left, right)] = True
            return True
        return False

    solns = []
    state = [] # no strings, also can reuse

    def backtrack(solns, state, idx):
        if idx == len(s):
            solns.append(state.copy())
        
        # select the next palindrome
        for end in range(idx, len(s)):
            if isPalindrome(idx, end):
                state.append(s[idx:end + 1])
                backtrack(solns, state, end + 1)
                state.pop()
    
    backtrack(solns, state, 0)
    return solns

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

            



