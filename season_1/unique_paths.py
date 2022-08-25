# Results:
# Runtime: 30ms 96.13%
# Memory Usage: 13.9MB 73.95%

"""
https://leetcode.com/problems/unique-paths/

m x n grid, start top left corner 
- move to bottom right corner [m-1][n-1]
can only move down or right

return num possible unique paths given m and n that robot can take to reach bottom right corner

Ideas 1:
is there a closed form formula? 
- need to take m steps down, n steps right. m + n steps total
- m + n choose smaller - how many different variations there are

m+n! / m! (m + n - n!) = m + n * ... * n + 1 / m! if we divide out n
- concern is overflow
- assume doing factorial is O(n) time. So this is O(m + n)

Idea 2: search algorithm / backtracking?
- do dfs, from each state can either go right or down
- if reach end square, terminate
O(m * n) time?
- D[i, j] = num ways to reach end from i, j
- Can do this, store indices i and j, if go left or right, add to index. check out of bounds,
but also can do dp so that if you reach the same square, 

Idea: DP / backtracking
- D[i, j] = num ways to reach i, j = D[i-1, j] + D[i, j-1]
- Or recursive search, if i, j is end, return 1. else return numPaths(left) + numPaths(down)
- if out of bounds, return 0
- also store D[i, j]
Time: all possible paths, basically. may need to recalculate if not stored.
- each square processed exactly once, so O(m x n)

Idea 2: DP but D[i, j] is num paths to i, j
Time: O(m x n)
"""

def numPathsToEndFrom(m, n, currM, currN, state):
	if (currM == m-1 and currN == n-1):
		state[currM][currN] = 1
	elif (currM >= m or currN >= n):
		return 0
	elif(state[currM][currN] is None):
		state[currM][currN] = numPathsToEndFrom(m, n, currM + 1, currN, state) + numPathsToEndFrom(m, n, currM, currN + 1, state)

	return state[currM][currN] # already solved this square

def backtrackingSoln(m, n):
	state = [[None for _ in range(n)] for _ in range(m)]
	return numPathsToEndFrom(m, n, 0, 0, state)


def closedSolution(m, n):
	# just do the calculation
	largerNum, smallerNum = (m - 1, n - 1) if m > n else (n - 1, m - 1)

	currMultiplier = largerNum + smallerNum
	top = 1
	while (currMultiplier > smallerNum):
		top *= currMultiplier
		currMultiplier -= 1
	
	# get bottom
	currMultiplier = largerNum
	bottom = 1
	while (currMultiplier > 0):
		bottom *= currMultiplier
		currMultiplier -= 1
	
	return int(top / bottom)

def validate(m, n, expected):
	soln = backtrackingSoln(m, n)
	if (soln != expected):
		print("Error")
		print(m)
		print(n)
		print("Result " + str(soln))
		print("Expected " + str(expected))

validate(3, 2, 3)