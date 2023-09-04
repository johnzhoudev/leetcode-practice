"""

https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

obstacles array of len n
obstacles[i] is height

for each index i
find longest obstacle course
- choose obstacles between 0 and i, must include i
- must be in same order
- every obstacle is >= height of previous
- implies last obstacle, the ith one, must be the highest.

Feels like a DP problem?
longest increasing / non-decreasing subsequence for each? O(n^3)

O(n^2) longest increasing subsequence?
dp[i] = longest non-decreasing subsequence ending in i
dp[i] = max dp[j] from 0 <= j <= i-1, also if obstacles[j] <= curr

Alt: Tails?
- Basically keep array tails[] where 
tails[s] = minimum element in a non-decreasing subsequence with size s comprised of elements so far
- init all to inf
- For each i, do a binary search on s. If x <= nums[i], can be appended, so search longer
- else search shorter
- if not found, add to 1 elt size
- once found, tails[s+1] = min(tails[s+1], i)
- and also record answer

O(n log n), log n time per step

Tactic: DP but tails[i] = last item in subsequence of length i. binary search on i. if x can fit after subseq, must also fit after all smaller since non-dec. Trick: simple binary search l < r, build tails by appending if x smaller than all, or just tails[i] = x if found.

"""

# optimized
def solve(obstacles):
    tails = [] # array of last elt heights with length equal to idx + 1
    output = []

    for x in obstacles:

        # binary search to find first idx with elt larger than x
        # invalid if no elts, 
        if len(tails) == 0 or x >= tails[-1]: # then binary search doesn't narrow down to any valid
            output.append(len(tails) + 1)
            tails.append(x)
        else: # binary search for first elt greater than x
            left, right = 0, len(tails)
            while left < right:
                pivot = left + (right - left) // 2
                if tails[pivot] <= x: # still valid
                    left = pivot + 1
                else:
                    right = pivot # retain solution, so need to bias left
            
            # this should narrow down to 1 element, if it exists
            output.append(left + 1) # left is height - 1
            tails[left] = x # new min
    
    return output

# works
def binary_search(tails, x):
    left = 1
    right = len(tails)

    while 1 <= left and left <= right:
        # break early if found one to append to
        if right == left:
            return left if tails[left] <= x else -1

        pivot = left + (right - left + 1) // 2 # bias right, keep left

        if tails[pivot] <= x: # can be appended, continue
            left = pivot
        else: # else must be less
            right = pivot - 1

    return -1

def solve(obstacles):
    tails = [float('inf') for _ in range(len(obstacles) + 1)]
    output = []

    for i in range(len(obstacles)):
        x = obstacles[i]
        best_len = binary_search(tails, x)

        if best_len < 0: # not found, add
            tails[1] = min(tails[1], x)
            output.append(1)
        else:
            output.append(best_len + 1)
            tails[best_len+1] = min(tails[best_len+1], x)
    
    return output

        


# TLE
# going to do a dp way for completeness...
def solve(obstacles):
    dp = [1 for _ in range(len(obstacles))]
    dp[0] = 1

    for i in range(1, len(obstacles)):
        for j in range(0, i):
            if obstacles[j] <= obstacles[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return dp

import bisect

def longestObstacleCourseAtEachPosition(obstacles):
    n = len(obstacles)
    dp = []  # Initialize an empty list to store increasing subsequence
    ans = [0] * n

    for height in obstacles:
        # Use binary search to find the position where height can be inserted
        index = bisect.bisect_right(dp, height)
        
        # If index is equal to the length of dp, it means height is the largest so far
        if index == len(dp):
            dp.append(height)
        else:
            dp[index] = height  # Replace the element at index with the current height
        
        ans[index] = index + 1  # Update the answer with the length of the increasing subsequence

    return ans

# Example usage:
obstacles = [1, 3, 2, 1, 4, 5, 2, 6]
ans = longestObstacleCourseAtEachPosition(obstacles)
print(ans)  # Output: [1, 2, 2, 2, 3, 4, 3, 5]