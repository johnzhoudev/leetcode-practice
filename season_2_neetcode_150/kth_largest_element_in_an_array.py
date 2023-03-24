"""

https://leetcode.com/problems/kth-largest-element-in-an-array/

- get kth largest element

IDea: use heap, better than sorting. min heap to get max

Better: Quickselect, O(n) average case assuming good split
- 

Tactic: Quickselect, either hoare partition or split into new arr. Careful when recursing right

"""

# quickselect but rebuilding arrays
# need to reassign array and stuff
def solveSimple(nums, k):
    k = len(nums) - k + 1 # now kth smallest

    while True:
        pivot = nums[len(nums) // 2] # bias right

        smaller = [x for x in nums if x < pivot]
        same = [x for x in nums if x == pivot]
        larger = [x for x in nums if x > pivot]

        if k <= len(smaller):
            nums = smaller
        elif k > len(smaller) + len(same):
            nums = larger
            k -= len(smaller) + len(same)
        else:
            return same[0]
    
    raise RuntimeError()

def hoarePartition(nums, pivotIdx, left, right):

    pivot = nums[pivotIdx]

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    swap(pivotIdx, right)
    rightStart = right
    while left <= right:
        if nums[left] >= pivot:
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left > right:
                break
            swap(left, right)
        left += 1
    
    swap(left, rightStart)
    # left is one right of right, that's the separator.
    return left

def solve(nums, k):
    k = len(nums) - k + 1
    
    left = 0
    right = len(nums) - 1

    leftOfPivot = 0

    while right - left + 1 > 1:
        pivot = hoarePartition(nums, left + (right - left + 1) // 2, left, right) # biases right
        numsOnLeft = pivot - leftOfPivot + 1 # includes pivot
        if leftOfPivot + numsOnLeft < k:
            left = pivot + 1
            leftOfPivot += numsOnLeft
        elif leftOfPivot + numsOnLeft > k:
            right = pivot - 1
        else:
            return nums[pivot]
    
    return nums[left]





import heapq

def solve(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
