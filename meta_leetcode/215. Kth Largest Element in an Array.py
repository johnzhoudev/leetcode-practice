"""

215. Kth Largest Element in an Array

- kth largest element in array
- just use heap?

O(n log k)

Quickselect: O(n) avg case, O(n^2) worst case

Tactic:
Quickselect, NOT HEAP! smaller, same, larger arrays, larger >= k -> go larger, larger + same < k -> go smaller, else same

"""

def solve(nums, k):

    while len(nums) > 0:
        pivot = len(nums) // 2 # bias right

        smaller = []
        same = []
        larger = []

        for num in nums:
            if num < nums[pivot]:
                smaller.append(num)
            elif num > nums[pivot]:
                larger.append(num)
            else:
                same.append(num)
        
        # check
        if len(larger) >= k: # more than k elements larger, so need to recurse on larger
            nums = larger
        elif len(larger) + len(same) < k: # element must be in smaller
            nums = smaller
            k -= len(larger) + len(same) # looking for the kth largest element of smaller
        else:
            return same[0]
    
    assert(False)

print(solve([3,2,3,1,2,4,5,5,6], 4))
