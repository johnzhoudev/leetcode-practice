# Results:
# Runtime: 62ms 61.47%
# Memory Usage: 14MB 43.62%

"""
https://leetcode.com/problems/unique-paths-ii/

Given m x n array grid
robot top left
move to bottom right
can only move down or right
Obstacle is 1, space is 0
Path cannot take obstacles.

Num possible unique paths?

Ideas: 
- Can't math compute this, need to do a search algorithm
- num paths from i, j = num paths from i + 1, j or i, j+1 provided not a rock.
	- recursive method. So keep trying to solve. In recursion, if out of bounds, return 0. also return 0 if rock.
	- but if found last place, return 1.
	- guaranteed to reach all locations since explors.

	- Though, can also save time if we cache the results

- for grid, d[i][j] = d[i+1][j] + d[i][j+1] provided in bounds
	- what are the base cases? along the top and left edges, can get there if no rock in way. else 0 ways.

- So same idea as recursive, but we solve iteratively from left to right, top to bottom. and fill base cases 1
	- if reachable since only straight line, but if hit rock, 0 since cannot go around.

O(nm) since we do a computation for each.

Is there any better way? well, have to consider all squares at least, so no.

Exercise: do both recursive and iterative.

Tactic: Dynamic programming, d[i][j] = how many paths to it. Careful with base cases and obstacles.

"""

# Num ways to get from i, j to end is from i + 1, j and from i, j+1 to end
# if out of bounds, return 0. no paths to end.
# if in obstacle, return 0.
# if in bounds, return left + down
# if at end, return 1! you represent one path that goes there.
# works, but not as fast. Recursive calls expensive!
def recurse(grid, row, col, n, m, state):
	if (row >= n or col >= m or grid[row][col] == 1):
		return 0
	elif (state[row][col] != None):
		return state[row][col]
	elif (row == n-1 and col == m-1):
		return 1
	else:
		state[row][col] = recurse(grid, row+1, col, n, m, state) + recurse(grid, row, col+1, n, m, state) # how to cache this?
		return state[row][col]

def recursiveMethod(grid):
	state = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] # row, col
	return recurse(grid, 0, 0, len(grid), len(grid[0]), state)


def iterativeMethod(grid):
	# create state and setup base cases
	n = len(grid)
	m = len(grid[0])
	state = [[None for _ in range(m)] for _ in range(n)] # row, col

	# Base case: if no rock in way, change to 1. else 0
	hitRock = False
	for i in range(n): # rows, vertical
		if (not hitRock and grid[i][0] == 1): hitRock = True
		state[i][0] = 0 if hitRock else 1
	
	hitRock = False
	for j in range(m):
		if (not hitRock and grid[0][j] == 1): hitRock = True
		state[0][j] = 0 if hitRock else 1
	
	# Iterative step. solve going right, using formula d[i][j] = d[i-1] + d[j-1]
	# d[i][j] = num ways to get to i, j
	for i in range(1, n):
		for j in range(1, m):
			# if rock, 0. else, use old solns.
			if (grid[i][j] == 1):
				state[i][j] = 0
			else:
				state[i][j] = state[i-1][j] + state[i][j-1] # rocks will be 0 too
	
	return state[n-1][m-1]

def validate(testGrid, expected):
	# result = iterativeMethod(testGrid)
	result = recursiveMethod(testGrid)
	if (result != expected):
		print("Error")
		print(testGrid)
		print("Result: " + str(result))
		print("Expected: " + str(expected))

validate([[0,0,0],[0,1,0],[0,0,0]], 2)
validate([[0,1],[0,0]], 1)