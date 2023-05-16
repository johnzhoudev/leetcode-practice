"""

https://leetcode.com/problems/set-matrix-zeroes/

- set whole rows and cols to 0
- must do in place

Ideas:
- first traverse to find 0 cols and rows
- for each row and col with a zero, do.
O(n^2)

Stop! Constant space required

Ideas:
- first pass, modify to -1
- 2nd pass, change all -1 to 0

Ideas 3:
- use row / col as indicators for 0 rows and 0 cols
- do all
- then stuff. kinda dumb.

Tactic: many ways. keep row / col set. Or, mark matrix as -1 seen. Or, use row / col in matrix and 2 flags for 0row/col.

"""

def solve(matrix):
    # edge case 0th row and col
    zerorow = False
    zerocol = False

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

                if i == 0:
                    zerorow = True
                if j == 0:
                    zerocol = True
    
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(len(matrix)):
                matrix[i][j] = 0
    
    if zerorow:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if zerocol:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    



# x, not constant space!
def solve(matrix):
    zeroCols = set()
    zeroRows = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroCols.add(j)
                zeroRows.add(i)
    
    for r in zeroRows:
        for j in range(len(matrix[0])):
            matrix[r][j] = 0

    for c in zeroCols:
        for j in range(len(matrix)):
            matrix[j][c] = 0
    
    return matrix
