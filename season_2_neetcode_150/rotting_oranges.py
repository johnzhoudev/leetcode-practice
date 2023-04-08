"""

https://leetcode.com/problems/rotting-oranges/

- rotting oranges expand

Idea:
- maintain set of rotting oranges
- once rotten, dfs in directions and add to new set
    - readd if a fresh orange is there and becomes rotten
- count until all done

- then check if any fresh oranges left

Time: O(n) to dfs each thing

Tactic: dfs from each rotten, do one iter at a time and count numIter. Careful when adding new orange, when add, mark as seen so not added twice
"""

def solve(grid):
    currentRotten = []
    nextRotten = []
    numIter = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                grid[row][col] = 0
                nextRotten.append((row, col))
    
    while nextRotten:
        currentRotten = nextRotten
        nextRotten = []
        while currentRotten:
            row, col = currentRotten.pop()
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 0
                    nextRotten.append((newRow, newCol))
        if nextRotten:
            numIter += 1
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return -1
    return numIter
            

