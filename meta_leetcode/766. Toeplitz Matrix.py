"""

766. Toeplitz Matrix

toeplitz if every diagonal has same elements top left to bottom right

Just check manually

to bottom and across top

Better: for each node, just check if up one and left one is same

Tactic:
for each node not on edge, check if up one and left one is same

"""

def solve(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] != matrix[r-1][c-1]: return False
    return True



def solve(matrix):

    # start
    def check(i, j):
        val = matrix[i][j]
        # while in bounds
        while 0 <= i and i < len(matrix) and 0 <= j and j < len(matrix[0]):
            if matrix[i][j] != val: return False
            i += 1
            j += 1
        return True

    # first check top ot bottom left side
    for row in range(len(matrix)):
        if not check(row, 0):
            return False

    # Now check for all on top row
    for col in range(1, len(matrix[0])):
        if not check(0, col):
            return False
    return True
    







