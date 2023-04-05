"""

https://leetcode.com/problems/n-queens/

- place n queens on an nxn chessboard

Idea:
- backtracking / search alg
    - place a queen
    - go to next available slot and place another queen
    - how to avoid duplicates?
        - place row by row / col by col, in order. that should avoid duplicates
    - keep track of space: once queen placed, mark all other slots as taken
    - once queen is popped, mark rows and cols as free, and also decrement numQueens looking at a square
    - So O(n) time to add / pop a queen

Time: O(total num configurations, n*n?) * O(n) time to gen and eval each soln

Better: reduce time by keeping track of cols, +/- diagonals to check if taken
y = x + b
b = y - x
y = -x + b
b = y + x
- can use b to identify diagonals

Tactic: Backtrack by adding row at a time (choosing which col to add). Track if square attacked using colSet, posDiag, negDiag calculating b = y - mx

"""

def solve(n):
    state = [['.' for _ in range(n)] for _ in range(n)]
    colSet = set()
    posDiag = set()
    negDiag = set()
    attackState = (colSet, posDiag, negDiag)

    solns = []

    def backtrack(state, attackState, row):
        nonlocal solns
        if row == n:
            stateCopy = [''.join(row) for row in state]
            solns.append(stateCopy)
        else:
            colSet, posDiag, negDiag = attackState
            for col in range(n):
                if col in colSet or (col - row) in posDiag or (col + row) in negDiag:
                    continue
                colSet.add(col)
                posDiag.add(col - row)
                negDiag.add(col + row)
                state[row][col] = 'Q'
                backtrack(state, attackState, row + 1)
                state[row][col] = '.'
                colSet.remove(col)
                posDiag.remove(col - row)
                negDiag.remove(col + row)
    
    backtrack(state, attackState, 0)
    return solns


def solveSlow(n):
    state = [['.' for _ in range(n)] for _ in range(n)]
    boardAttacking = [[0 for _ in range(n)] for _ in range(n)]
    solns = []

    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    def addQueen(boardAttacking, row, col):
        for i in range(n):
            boardAttacking[row][i] += 1
            boardAttacking[i][col] += 1
        # boardAttacking[row][col] -= 2

        for dx, dy in directions:
            x, y = row, col
            while 0 <= x and x < n and 0 <= y and y < n:
                boardAttacking[x][y] += 1
                x += dx
                y += dy
        # boardAttacking[row][col] -= 4

    def removeQueen(boardAttacking, row, col):
        for i in range(n):
            boardAttacking[row][i] -= 1
            boardAttacking[i][col] -= 1

        for dx, dy in directions:
            x, y = row, col
            while 0 <= x and x < n and 0 <= y and y < n:
                boardAttacking[x][y] -= 1
                x += dx
                y += dy

    def backtrack(solns, state, boardAttacking, row):
        if row == n: # added n queens
            stateCopy = [''.join(row) for row in state]
            solns.append(stateCopy)
        else:
            # add next queen to next row, choose next column
            for col in range(n):
                if boardAttacking[row][col] == 0:
                    addQueen(boardAttacking, row, col)
                    state[row][col] = 'Q'
                    backtrack(solns, state, boardAttacking, row + 1)
                    state[row][col] = '.'
                    removeQueen(boardAttacking, row, col)
    
    backtrack(solns, state, boardAttacking, 0)
    return solns


