"""

162. Find Peak Element

element strictly greater than neighbours
- elements next to edges are always greater

Must run in O(log n) time

Say you pick a random number:

[1,2,1,3,5,6,4]

- if 1, both 2 and 3 larger. so peak elt could be in either side.
    - but if number is larger, implies a peak element is in both sides
- if only 1 larger, go that side.
- if both smaller, peak elt. return

O(log n)

Tactic:
Binary search, go in direction where neighbour is larger.

"""

def solve(nums):

    def isNeighbourSmaller(idx, dir, left, right):
        nidx = idx + dir
        # out of bounds
        if not (left <= nidx and nidx <= right):
            return True
        
        return nums[idx] > nums[nidx] # is neighbour smaller

    left = 0
    right = len(nums) - 1

    while left < right:
        pivot = left + (right - left) // 2 # bias left

        leftSmaller = isNeighbourSmaller(pivot, -1, left, right)
        rightSmaller = isNeighbourSmaller(pivot, 1, left, right)

        if leftSmaller and rightSmaller:
            return pivot
        elif leftSmaller: # right larger, so go right
            left = pivot + 1
        else: # left larger, so go left
            right = pivot - 1
    
    raise RuntimeError()


print(solve([1,2,3,1]))

        
