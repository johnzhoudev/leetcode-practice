"""

Given integer array nums
find subarray with largest sum

Must be non-empty

Tactic: Sliding window, either take the number with the current or just take the number and start anew

O(n)

Challenge: Divide and conquer approach?


Divide and conquer
- Split to left and right
- need to know best of each side + best partial of left and best partial of right
    - so need to return total sum + best partial left + best partial right + best

Base case: 1 element
- total = elt, best partial left = elt or None, best partial right = elt or None, best = elt or None

- total = sum of a and b, best partial left = best partial left of left or all of left + best partial left of right or don't use
best = max best of left, best of right, best partial left + best partial right

"""
def solve(nums):
    # O(n log n) runtime since have to split recursively
    

    def helper(l, r): # return total, best_from_left, best_from_right, best. Array indices exclusive
        length = r - l
        if length == 1:
            x = nums[l]
            return x, x, x, x
        
        # Else, split in 2
        pivot = l + ((r - l) // 2)
        left = helper(l, pivot) # exclusive
        right = helper(pivot, r) # bias right, right is larger

        total = left[0] + right[0]
        best_from_left = max(left[1], left[0] + right[1])
        best_from_right = max(right[2], right[0] + left[2])
        best = max(left[3], right[3], left[2] + right[1])
        return total, best_from_left, best_from_right, best
    
    res = helper(0, len(nums))
    return res[3]


# def solve(nums):

#     def helper(arr): # return total, best_from_left, best_from_right, best
#         if len(arr) == 1:
#             return arr[0], arr[0], arr[0], arr[0]
        
#         # Else, split in 2
#         left = helper(arr[:len(arr)-1])
#         right = helper(arr[len(arr)-1:]) # bias left, right is smaller

#         total = left[0] + right[0]
#         best_from_left = max(left[1], left[0] + right[1])
#         best_from_right = max(right[2], right[0] + left[2])
#         best = max(left[3], right[3], left[2] + right[1])
#         return total, best_from_left, best_from_right, best
    
#     res = helper(nums)
#     return res[3]


def validate(arr, expected):
    res = solve(arr)
    if res != expected:
        print(f"{arr} generated {res}, expected {expected}")


validate([-2,1,-3,4,-1,2,1,-5,4], 6)



def solve(nums):
    best = nums[0]
    total = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < total + nums[i]: # better to continue range
            total += nums[i]
        else: # Start anew
            total = nums[i]
        best = max(best, total)
    return best



