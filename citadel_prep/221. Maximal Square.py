"""

221. Maximal Square

find largest square containing only 1's
and return area


Preprocess:
- for each i,j, rightwards and downwards longest string of consecutive 1's
- then it's faster to make square
- only search larger square too? from top left corner


O(n^2m) too slow

It's fucking DP??!?!??!?!?!!?!!!!!
I mean makes sense, smaller rect to bigger rect

dp[i][j] = from up, left, and upleft min + 1 => if you think about it, if you have a big square, top and left edge will be 
at least 1, then inner at least 2, and so on.

Tactic:
DP: dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1 if matrix[r][c] == 1. Then max is max edge length!

"""

def solve(matrix):
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    best=0

    # base cases
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '1':
                best = 1
                dp[r][c] = 1
    
    # print(dp)
    # dp
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[r][c] == '0': continue
            dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
            best = max(best, dp[r][c])
    
    # for r in dp:
    #     print(r)
    return best ** 2
    
print(solve([["0","1"],["1","0"]]))

def solve(matrix):

    ones = []
    for r in range(len(matrix)):
        maxOnes = []
        seen = 0
        for c in range(len(matrix[0])-1, -1, -1):
            if matrix[r][c] == '1':
                seen += 1
            else:
                seen = 0
            maxOnes.append(seen)
        ones.append(maxOnes[::-1]) # reverse
    
    # ones now contains number of continuous ones to the right
    # brute force, just check every corner

    def getLargestSquare(r, c):
        nonlocal ones

        vertSize = 1
        minLongSize = ones[r][c]

        while True:
            vertSize += 1
            if r + vertSize - 1 >= len(ones): break
            minLongSize = min(minLongSize, ones[r + vertSize - 1][c])
            if vertSize > minLongSize: break

        return (vertSize - 1) ** 2

    best = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != '1': continue
            best = max(getLargestSquare(r, c), best)
    return best


            

            

print(solve([["1","1"],["1","1"]]))
            


