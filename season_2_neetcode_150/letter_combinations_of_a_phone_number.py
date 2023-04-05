"""

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

- map digits 2 to 9
- these map to letters
- return all combos

Idea:
- search alg, build based on next letters
Time: O(3**n) or number of combos, find each one in O(1)
Space: O(n), if we reuse

Tactic: Hardest part transform digits to next letters. Otherwise classic backtracking. ''.join(list) helps
"""

def solve(digits):
    solns = []
    state = []

    def digitToLetters(d):
        if d == 7: return ['p', 'q', 'r', 's']
        if d == 8: return ['t', 'u', 'v']
        if d == 9: return ['w', 'x', 'y', 'z']
        d = d-2
        mult = d
        out = []
        for off in (0, 1, 2):
            out += [chr(ord('a') + 3*mult + off)]
        return out
    
    def backtrack(solns, state, idx):
        if idx == len(digits):
            solns.append(''.join(state))
        else:
            for nextChar in digitToLetters(int(digits[idx])):
                state += [nextChar]
                backtrack(solns, state, idx + 1)
                state.pop()
    
    if len(digits) == 0:
        return []
    backtrack(solns, state, 0)
    return solns
        