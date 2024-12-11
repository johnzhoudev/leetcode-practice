"""48. Rotate Image

rotate 90 degrees clockwise
must do it in place

Either flip flop

Or rotate each layer

rotate Groups of 4 cells

(loop, loop + offset)        (loop + offset, n - 1 - loop)
(n - 1 - loop - offset, loop)                          (n - 1 - loop, n - 1 - loop - offset)   

Tactic:
Flip vert + flip diag, or flip pairs of 4 - loop var (n // 2), and offset (n - (2 * loop) - 1)

"""

def solve(matrix):
    n = len(matrix)
    for loop in range(n // 2): # 0,0
        for offset in range(n - (2 * loop) - 1): # doing 1 too many
            temp = matrix[loop][loop + offset]
            matrix[loop][loop + offset] = matrix[n - 1 - loop - offset][loop]
            matrix[n - 1 - loop - offset][loop] = matrix[n - 1 - loop][n - 1 - loop - offset]
            matrix[n - 1 - loop][n - 1 - loop - offset] = matrix[loop + offset][n - loop - 1]
            matrix[loop + offset][n - loop - 1] = temp
    
    
        

# modify in place
def solve(matrix):

    def swap(i, j, i2, j2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i2][j2]
        matrix[i2][j2] = temp

    def flipHorizontally(matrix):
        for row in range(len(matrix) // 2):
            for col in range(len(matrix[0])):
                swap(row, col, len(matrix) - 1 - row, col)
    
    def flipDiagonally(matrix):
        # row col becomes col row
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                swap(row, col, col, row)

    flipHorizontally(matrix)
    flipDiagonally(matrix)




