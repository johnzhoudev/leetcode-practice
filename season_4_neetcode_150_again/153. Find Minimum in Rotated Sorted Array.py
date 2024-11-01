"""

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n 
times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[2,3,4,5,6,1,1.1, 1.2, 1.3] if it was rotated 6 times.
[2,3,4,5,6,7] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Ideas:
- do a binary search

[1, 2, 3, 4]
[4, 1, 2, 3]
[2, 3, 4, 1]

"""

def solve(arr):
    left = 0
    right = len(arr) - 1 

    while left <= right:
        if right - left + 1 == 2: return min(arr[left], arr[right])
        if left == right: return arr[left] # found solution

        pivot = left + (right - left) // 2 # bias left
        leftVal = arr[left]
        rightVal = arr[right]
        val = arr[pivot]

        # we need to check the left and right ends and see if there's a wrap around
        if leftVal <= val and rightVal >= val:
            right = pivot - 1
        elif leftVal > val: # left wraparound, go left 
            right = pivot
        else: # rightval < current val
            left = pivot + 1
    
    raise RuntimeError()

def validate(testArr, expected):
    res = solve(testArr)
    if res == expected: print("Success! Got ", res)
    else:
        print("Failed", testArr, expected)
        print("Got", res)


validate([1, 2, 3, 4], 1)
validate([2, 3, 4, 1], 1)
validate([4, 1, 2, 3], 1)
validate([4, 5, 1, 2, 3], 1)
validate([3, 4, 5, 1, 2], 1)
