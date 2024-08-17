"""

return all possible n queen outcomes

Search algorithm

- for each queen, decide where you can put it and continue
    - can't put queen past a certain point to avoid repeats
- maintain sets for rows, cols and diagonals with a queen
- or maintain sets of rows, cols and diagonals that are free?
- put n queens, so pick for every row and col

- so to pick new, pick row, and for each free col check diagonal.

"""

def solve(n):
    UP = "up"
    DOWN = "down"

    usedCols = set()
    usedDiagDown = set()
    usedDiagUp = set()
    # accessed by y intercept

    # y = mx + b
    # col - m * row = b
    def getYIntercept(row, col, dir):
        if dir == UP:
            return col - row
        return col + row

    output = []
    state = []

    def dfs(row):
        nonlocal usedCols
        nonlocal usedDiagDown
        nonlocal usedDiagUp
        nonlocal state
        nonlocal output

        if row >= n:
            output += [state.copy()]

        # pick next valid
        for col in range(n):
            diagUp = getYIntercept(row, col, UP)
            diagDown = getYIntercept(row, col, DOWN)
            if col in usedCols or diagUp in usedDiagUp or diagDown in usedDiagDown:
                continue # invalid 

            # mark
            usedCols.add(col)
            usedDiagDown.add(diagDown)
            usedDiagUp.add(diagUp)
            state += ['.' * col + 'Q' + '.' * (n - (col + 1))]
            dfs(row + 1)
            state.pop()
            usedCols.remove(col)
            usedDiagDown.remove(diagDown)
            usedDiagUp.remove(diagUp)
    
    dfs(0)
    return output