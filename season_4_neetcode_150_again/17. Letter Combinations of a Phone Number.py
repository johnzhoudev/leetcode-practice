"""

contains 2 to 9

Idea:
- backtracking choice at each step

"""

def solve(digits):

    def mapDigit(digit):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        digit = int(digit)
        if 2 <= digit and digit <= 6:
            offset = digit - 2
            return alphabet[offset * 3:offset*3 + 3]
        elif digit == 7:
            return "pqrs"
        elif digit == 8:
            return "tuv"
        elif digit == 9:
            return "wxyz"
    
    output = []

    def dfs(text, i): # i is next digit
        nonlocal output
        if i >= len(digits):
            output += [text]
            return

        # else continue exploring
        for c in mapDigit(digits[i]):
            dfs(text + c, i + 1)
    
    if len(digits) == 0: return []
    dfs("", 0)
    return output
        



