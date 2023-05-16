"""

https://leetcode.com/problems/spiral-matrix/

Ideas:
- direction array, advance until out of bounds or seen. Then continue in next direction
- finished when, just after dir switch, next is also out of bounds

Tactic: while x, y valid, output. mark as seen. adv, and if out of bounds, change dir.
"""

def solve(matrix):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    n, m = len(matrix), len(matrix[0])
    output = []

    currDir = 0
    dx, dy = directions[currDir]

    while (0 <= x and x < n and 0 <= y and y < m) and matrix[x][y] != -404:
        # add current
        output.append(matrix[x][y])
        matrix[x][y] = -404

        # try to advance
        x += dx
        y += dy

        # if out of bounds or seen, direction change
        if not (0 <= x and x < n and 0 <= y and y < m) or matrix[x][y] == -404:
            x -= dx
            y -= dy
            currDir = (currDir + 1) % 4
            dx, dy = directions[currDir]
            x += dx
            y += dy
        
    return output



