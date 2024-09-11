"""

matrix - X and 0's capture regions that are surrounded

- So basically, like water flow question. 

Idea:
- do dfs from all edges for O's => these are O's that are not captured.
- others are surrounded

- 1 pass convert all O's to Y's
- 2nd pass to convert O's to x's and Y's to O's

O(n) time O(1) space since space used is part of board


do it iteratively?
"""

def solve(board):

    state = []
    # add all edges if have an O
    for r in range(len(board)):
        if board[r][0] == 'O':
            state.append((r, 0))
        if board[r][len(board[0]) - 1] == 'O':
            state.append((r, len(board[0]) - 1))

    for c in range(len(board[0])):
        if board[0][c] == 'O':
            state.append((0, c))
        if board[len(board) - 1][c] == 'O':
            state.append((len(board) - 1, c))
    
    # corners added twice
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def isInBounds(x, y):
        return 0 <= x and x < len(board) and 0 <= y and y < len(board[0])
    while state:
        x, y = state.pop()
        if not isInBounds(x, y): continue
        if board[x][y] == 'O':
            board[x][y] = 'Y'

            for dx, dy in directions:
                state.append((x + dx, y + dy))
    
    # now second pass to convert again
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'Y':
                board[r][c] = 'O'
            elif board[r][c] == 'O':
                board[r][c] = 'X'





