"""

https://leetcode.com/problems/kth-largest-element-in-an-array/


IDea: use heap, better than sorting. min heap to get max

Better: Quickselect, O(n) average case assuming good split
- 

"""

def hoarePartition(nums, pivotIdx, left, right):

    pivot = nums[pivotIdx]

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while left <= right:
        if nums[left] >= pivot:
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left > right:
                break
            swap(left, right)
        left += 1
    
    # left is one right of right, that's the separator.
    return left

x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
print(hoarePartition(x, 4, 0, len(x) - 1))
print(x)

def solve(nums, k):
    k = len(nums) - k + 1
    
    left = 0
    right = len(nums) - 1

    leftOfPivot = 0

    while right - left + 1 > 1:
        pivot = hoarePartition(nums, left + (right - left + 1) // 2, left, right) # biases right
        numsOnLeft = pivot - leftOfPivot # includes pivot
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
