"""

498. Diagonal Traverse

just use directions to traverse


Tactic:

Intuitive solution, keep directions + at end, where to head 1 vs 2. Then just simulate. It's a bit slow but asymptotically, it's fine. Out of bounds check to know when to switch.

There exist tricks, like r + c % 2 == 0 => moving up, == 1 => moving down. But can't be bothered.

"""

def solve(matrix):

    directions = [((-1, 1), (0, 1), (1, 0)), ((1, -1), (1, 0), (0, 1))] # (traverse dir) (reached end, try go this way) (if not, go this way)
    dir = 0

    def isInRange(x, y):
        return 0 <= x and x < len(matrix) and 0 <= y and y < len(matrix[0])
    
    r = 0
    c = 0
    
    output = []
    while True:
        output.append(matrix[r][c])
        dr, dc = directions[dir][0]

        # take a step
        newR = r + dr
        newC = c + dc

        # if out of bounds, try to take other steps and change dir
        if not isInRange(newR, newC):
            # try resetting
            for dr1, dc1 in directions[dir][1:]:
                if isInRange(r + dr1, c + dc1):
                    newR = r + dr1
                    newC = c + dc1
                    dir = 1 - dir
                    break
            
        if not isInRange(newR, newC): break
        # now add to output
        r = newR
        c = newC
    
    return output


        




