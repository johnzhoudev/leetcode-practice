"""

79. Word Search

given grid and word, true if word exists in grid. cannot reuse cells

Idea:
- dfs from each starting point, fail if not part of character
O(mn * word len)

"""

def solve(board, word):

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # m x n grid
    m = len(board)
    n = len(board[0])

    found = False

    def dfs(i, j, visited, wordIdx):
        nonlocal found
        assert wordIdx < len(word)

        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or word[wordIdx] != board[i][j]:
            return # invalid
        elif wordIdx + 1 == len(word): # if completed word
            found = True
            return
        
        # otherwise, search
        visited.add((i, j))
        wordIdx += 1
        for dx, dy in directions:
            dfs(i + dx, j + dy, visited, wordIdx)
        visited.remove((i, j))
        wordIdx -= 1

        return
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited = set()
            dfs(i, j, visited, 0)

            if found: return found
    
    return found


