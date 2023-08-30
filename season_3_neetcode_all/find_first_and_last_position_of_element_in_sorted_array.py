"""

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

nums non decreasing
find starting and ending position of target number


Idea:

Binary search, with mastery of bias
- find left and right index, 2 searches

Tactic: Binary search for 2 boundaries, bias left and maintain left vs bias right and maintain right


"""

def solve(nums, target):

    def find_left_idx(nums, target):
        left = 0
        right = len(nums) - 1 # inclusive range

        while 0 <= left and left <= right:
            pivot = left + (right - left) // 2 # bias left
            val = nums[pivot]
            if val < target:
                left = pivot + 1
            elif val > target:
                right = pivot - 1
            else: # val == target, but want leftmost so bias left
                # return if only one elt
                if right - left + 1 == 1:
                    return pivot
                right = pivot # still valid
        return -1 # not found

    def find_right_idx(nums, target):
        left = 0
        right = len(nums) - 1 # inclusive range

        while 0 <= left and left <= right:
            pivot = left + (right - left + 1) // 2 # bias right
            val = nums[pivot]
            if val < target:
                left = pivot + 1
            elif val > target:
                right = pivot - 1
            else: # val == target, but want leftmost so bias left
                # return if only one elt
                if right - left + 1 == 1:
                    return pivot
                left = pivot # still valid
        return -1 # not found
    
    left = find_left_idx(nums, target)
    right = find_right_idx(nums, target)
    return [left, right]



