"""

3066. Minimum Operations to Exceed Threshold Value II

nums, k
remove x and y from nums (arbitrary, must be 2 smallest )
min(x,  y) * 2 + max(x, y)

Isn't it fixed? 
put them all in a heap and figure out?
O(n log n)???

double min + max

x y z
2x + y, z
4x + 2y + z or 2z + 2x + y

"""

import heapq

def solve(nums, k):

    heapq.heapify(nums)
    numOp = 0

    while len(nums) >= 2:
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        if num1 >= k: return numOp
        heapq.heappush(nums, num1 * 2 + num2)
        numOp += 1

    return numOp




