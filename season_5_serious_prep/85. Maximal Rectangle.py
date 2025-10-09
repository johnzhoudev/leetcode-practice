"""

largest rectangle containing only 1's and return its area

How to find rectangles? Some BFS or dfs surely

Brute force: O(n^3), pick corners and check all squares

DP O(n^2)? all rectangles 1xn, 2xn, ...
- 2xn if 2 1xn's can figure out in O(1)



x x x
x x x
x x x
x x x

dp[(x, y), (x2, y2)] = dp[x, y, x2-1, y2] and dp[x2, y, x2, y2-1]

THIS IS TLE???

Might need to prune.

Can do 1 starting point, increasing rectangle size l->r, u->d
From left to right, just keep track of how far right you can go. Should cut out some cases.
So that way you're only checking potential possible rectangles. Should cut out a lot.

Only need to keep dp for each starting point, so O(n) space

Best:

Add each row at a time and have a histogram, then get best rectangle area in a histogram.
- as you go, keep monotonic increasing heights (anything smaller than last, will have less area)
- each column must be >= previous heights, then get max area.
- at the end, if still left, then multiply by whole thing
O(n)

Then do this for each row
O(n) in total, processing each element once


Tactic: Solve max area in histogram, and do that row by row for the matrix. 
To solve max area in histogram, monotonic inc list of heights. When u add smth smaller, popped are the "ends". 
And your new column that you add becomes the left edge height with popped idxs (since popped ones can be considered left edge still)

"""

def solve(matrix):
    best = 0

    def solve_histogram(cols):
        best = 0
        previous_large_cols = [] # (height, col_idx)
        for idx, col in enumerate(cols):

            new_idx = idx
            while previous_large_cols and col < previous_large_cols[-1][0]: # current is smaller than largest
                prev, prev_idx = previous_large_cols.pop()
                best = max(best, prev * (idx - prev_idx))
                new_idx = prev_idx # the one you deleted is larger than curr, so curr is effectively now the prev_idx
            
            # calculate area 
            previous_large_cols.append((col, new_idx))
        
        # At end, if any still left, calc area with length of array
        for prev, prev_idx in previous_large_cols:
            best = max(best, prev * (len(cols) - prev_idx))
        
        return best
    
    # Test cases for solve_histogram
    # assert(solve_histogram([1]) == 1)
    # assert(solve_histogram([2, 0, 1]) == 2)
    # assert(solve_histogram([0, 1, 2, 2, 3]) == 6)
    # assert(solve_histogram([]) == 0)
    # assert(solve_histogram([3, 3, 3, 2, 2, 2, 1]) == 12)
    # assert(solve_histogram([2, 2, 2, 3, 3, 3, 1]) == 12)
    # assert(solve_histogram([3, 2, 1, 0]) == 4)

    cols = [0 for _ in range(len(matrix[0]))]
    best = 0
    for row in matrix:
        for idx, elt in enumerate(row):
            if elt == '1':
                cols[idx] += 1
            else:
                cols[idx] = 0
        best = max(best, solve_histogram(cols))
    return best



def solve3(matrix):

    best = 0

    for row_start in range(len(matrix)):
        for col_start in range(len(matrix[0])):
            dp = set() # start dp, contains coords (x2, y2) for rectangles that are valid

            max_col = len(matrix[0])

            for end_row in range(row_start, len(matrix)):
                for end_col in range(col_start, max_col):
                    x, y = (row_start, col_start)
                    x2, y2 = (end_row, end_col)

                    # Base cases
                    if x == x2 and y == y2 and matrix[x][y] == '1': # Single point
                        dp.add((x2, y2))
                    else:
                        if x2-1 < x:
                            bottom_rect = True
                        else:
                            bottom_rect = (x2-1, y2) in dp

                        if y2-1 < y:
                            left_rect =  True
                        else:
                            left_rect = (x2, y2-1) in dp

                        if bottom_rect and left_rect and (matrix[x2][y2] == '1'):
                            dp.add((x2, y2))
                        else:
                            # Prune columns
                            max_col = min(max_col, y2) # y2 has a 0
                            break # Stop col loop
                    
                    if (x2, y2) in dp: # If found, take max area
                        best = max(best, abs((y2-y + 1) * (x2-x + 1)))

    return best


def solve2(matrix):
    # DP from top down, left to right
    dp = set() # access with ((x, y), (x, y)) rectangle, true or False

    best = 0

    # Iterate thru all sizes, going top to down, left to right
    for num_rows in range(1, len(matrix) + 1):
        for num_cols in range(1, len(matrix[0]) + 1):
            for row_start in range(len(matrix) - num_rows + 1):
                for col_start in range(len(matrix[0]) - num_cols + 1):

                    x, y = (row_start, col_start)
                    x2, y2 = (row_start + num_rows - 1, col_start + num_cols - 1)

                    # Base cases
                    if num_rows == 1 and num_cols == 1 and matrix[x][y] == '1':
                        dp.add((x, y, x2, y2))
                    else:
                        if x2-1 < x:
                            bottom_rect = True
                        else:
                            bottom_rect = (x, y, x2-1, y2) in dp

                        if y2-1 < y:
                            left_rect =  True
                        else:
                            left_rect = (x2, y, x2, y2-1) in dp

                        if bottom_rect and left_rect and (matrix[x2][y2] == '1'):
                            dp.add((x, y, x2, y2))
                    
                    if (x, y, x2, y2) in dp:
                        best = max(best, abs((y2-y + 1) * (x2-x + 1)))

    return best

def check(arr, expected):
    res = solve(arr)
    if res != expected:
        print("Error, expected", expected, "got", res)

check([
    ['1', '1', '0'],
    ['1', '1', '0'],
    ['1', '1', '0'],
    ['1', '1', '0'],
], 8)

check(['1'], 1)
check(['0'], 0)
check(['0', '0', '0'], 0)
check(['0', '0', '1'], 1)
check(['0', '1', '0'], 1)
check([
    ['0', '1'],
    ['1', '1'],
], 2)


check([
    ['0', '1'],
    ['0', '1'], 
], 2)





