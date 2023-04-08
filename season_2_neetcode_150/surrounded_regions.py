"""

https://leetcode.com/problems/surrounded-regions/

- flip x to 0 if on border or connected to border

Idea:
- dfs from borders, mark as safe, everything else as dead
- Do dfs from each edge, mark all as j, then remove all that aren't found
Time: O(n), space: O(n) but in output size / modify in place

Can't do a one shot recursive because that relies on finding ocean in the last step

Tactic: DFS from edges. Make sure don't nest for loop when adding edges. either mark as reached or maintain set of visited

"""

def solve(board):
    state = []
    for row in range(len(board)):
        state.extend([(row, 0), (row, len(board[0])-1)])
    for col in range(len(board[0])):
        state.extend([(0, col), (len(board)-1, col)])

    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while state:
        row, col = state.pop()
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in visited:
            continue
        visited.add((row, col))
        if board[row][col] == "X":
            continue
        if board[row][col] == "O":
            board[row][col] = "k"
        
        for dr, dc in directions:
            state.append((row + dr, col + dc))
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "k":
                board[row][col] = "O"
            elif board[row][col] == "O":
                board[row][col] = 'X'



        