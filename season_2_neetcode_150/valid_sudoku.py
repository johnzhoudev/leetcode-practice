# Results:
# Runtime: 95ms 81.96%
# Memory Usage: 13.9MB 74.50%

"""

https://leetcode.com/problems/valid-sudoku/

O(n) time, 3 passes, to check each cell clear. Each cell checked 3 times
- use sets

Tactic: 3 passes, use sets to check. And make helper func to validate

"""

def solve(board):
    # do 3 passes

    n = len(board)
    assert(n == 9)

    validDigits = "123456789"
    currentDigits = set()

    def validateNewDigit(char, currentDigits):
        nonlocal validDigits
        if char == '.':
            return True
        elif char not in validDigits or char in currentDigits:
            return False
        else:
            currentDigits.add(char)
            return True

    # check each row is valid
    for row in range(n):
        for col in range(n):
            char = board[row][col] 
            if validateNewDigit(char, currentDigits) is False:
                return False
        
        # if got here, ran for each col, so row valid. reset state
        currentDigits.clear()
    
    # now check each col is valid
    for col in range(n):
        for row in range(n):
            char = board[row][col] 
            if validateNewDigit(char, currentDigits) is False:
                return False
        
        # if got here, ran for each col, so row valid. reset state
        currentDigits.clear()
    
    # Now check for squares
    for squareRow in range(3):
        for squareCol in range(3):
            for row in range(3):
                for col in range(3):
                    char = board[squareRow * 3 + row][squareCol * 3 + col]
                    if validateNewDigit(char, currentDigits) is False:
                        return False
        
            currentDigits.clear()
    
    return True




            




