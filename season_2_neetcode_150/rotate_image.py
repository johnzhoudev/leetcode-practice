"""

https://leetcode.com/problems/rotate-image/

- rotate image 90 degs clockwise
- must rotate array in place!

Brute force: 4 pairs
- for each ring
- start, direction, offset
- swap with temp

Ideas:
- since have to do it in place, need to swap

Either do in pairs of 4
Or, transpose and reverse **

Tactic: Transpose and reverse, or 4 pairs. If doing 4 pairs, consider l/r bounds and i, and swap all 4 manually. Careful, don't need to swap last. also careful with offsets.

"""

def solve(matrix):
    l, r = 0, len(matrix) - 1

    while l < r:
        top, bottom = l, r
        for i in range(r - l):
            temp = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = temp
    return matrix





# 4 pairs version
def solve(matrix):

    def swap(i, j, i2, j2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i2][j2]
        matrix[i2][j2] = temp
    
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    # for each ring size
    n = len(matrix)
    while n > 1:
        start = ((len(matrix) - n) // 2)
        end = start + n - 1
        corners = [(start, end), (end, end), (end, start), (start, start)]

        # now for each offset / pair, rotate
        # CAREFUL!!! Don't need to swap the last element
        for off in range(n-1):
            # fill with first element
            temp = matrix[start][start + off]
            for i in range(4):
                # extract next location
                x, y = corners[i]
                dx, dy = directions[i]
                dx *= off
                dy *= off
                x += dx
                y += dy

                temp2 = matrix[x][y]
                matrix[x][y] = temp
                temp = temp2

        n -= 2

    return matrix

def solve(matrix):
    # first do transpose

    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i] 
            matrix[j][i] = temp
    
    # then do reverse
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix[i]) - j - 1]
            matrix[i][len(matrix[i]) - j - 1] = temp

    
    return matrix