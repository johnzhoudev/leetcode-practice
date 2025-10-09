"""

540. Single Element in a Sorted Array

binary search, using index 

- check left and right
- if index is even, match on right - if on left, number is to right
- if index is odd, match on left - if on left, number is to left

"""



def solve(nums) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        pivot = left + (right - left) // 2 # Bias left
        
        left_elt = nums[pivot-1] if pivot > 0 else None
        right_elt = nums[pivot+1] if pivot < len(nums) - 1 else None
        elt = nums[pivot]

        if (pivot % 2) == 0: # even
            if elt == right_elt: # num is to right
                left = pivot + 1
            elif elt == left_elt:
                right = pivot - 1
            else:
                return nums[pivot]
        else:
            if elt == right_elt: # num is to left
                right = pivot - 1
            elif elt == left_elt:
                left = pivot + 1
            else:
                return nums[pivot]

    return nums[left]


def test(expected, inp):
    res = solve(inp)
    if not expected == res:
        print("expected", expected, "got", res)

test(2, [1, 1, 2, 3, 3, 4, 4, 8, 8])
test(1, [1])
test(1, [1, 2, 2])
test(2, [1, 1, 2])
