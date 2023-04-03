"""

https://leetcode.com/problems/word-search/

given board and word, return true / false
- can be in any direction, but cannot reuse a cell

Idea:
- search algorithm, can do iterative, must match the word.
    - or do recursive, and maintain visited
Time: O(m * n * len word), pretty hard to compute.

Tactic: Backtracking / dfs, recursive with visited. Can check early if too many letters in word, or frequency.

"""

def solve(board, word):

    visited = set()
    n = len(board)
    m = len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Optimization
    if len(word) > n * m:
        return False
    
    boardLetters = {}
    for row in board:
        for l in row:
            if l not in boardLetters:
                boardLetters[l] = 0
            boardLetters[l] += 1
    wordLetters = {}
    for l in word:
        if l not in boardLetters: return False
        if l not in wordLetters:
            wordLetters[l] = 0
        wordLetters[l] += 1
    
    for letter in wordLetters:
        if wordLetters[letter] > boardLetters[letter]:
            return False
    # end of optimization

    isFound = False

    def dfs(i, row, col, visited): # i is curr index in word, hasn't matched yet
        nonlocal isFound

        if i == len(word):
            isFound = True
            return

        # out of bounds
        if row < 0 or row >= n or col < 0 or col >= m or (row, col) in visited:
            return

        # add current position
        if board[row][col] == word[i]:
            visited.add((row, col))

            for dx, dy in directions:
                dfs(i+1, row + dx, col + dy, visited)
                if isFound: return

            visited.remove((row, col))
        
    # for each starting point
    for row in range(n):
        for col in range(m):
            if isFound: return isFound
            dfs(0, row, col, set())

    return isFound




