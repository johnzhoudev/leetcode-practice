"""

4. Median of Two Sorted Arrays

2 sorted arrays
return median


Idea:
Binary search

Even or odd total numbers, bias left - find number st nums to left and it make up ceil(n / 2)
- numNumbers - 

if you pick index i in array 1

then i + 1 nums to left and it in array 1 and len(a1) - i - 1 nums to the right

then need
(len(a1) + len(a2)) // 2  (floor) = i + 1 + k + 1

Idea 

1 2 3 4 5 inf
- 1 3 4 inf
- 2 5

- say we picked 4
- 3 elts to left, so need all elts in other array on right
- but 2 < 4

say we picked 2
- 1 elt to left, 1 to right
- so we need 1 elt to left and 2 to right (bias left)
- 1 and 2 need oto be less than 3 and 5 => true, so since odd, take middle - 1

1 2 3 4 5 6
- 1 4 5
- 2 3 6

Edge case
4 5 6
1 2 3

- say we pick 1
- 4 elts in total
- 4 is the next element
- so in array 2, splitting in half, we need 2 and 1 to be <= 3 and 4 => true
    - then take median of those elements

Edge Case: picking edge
- if we picked 4, 
    - 2 elts behind it in first 
    - so 2 must be larger than 4 - not true!
    - 2 smaller than 4, so we picked too far right. Go left.

Tactic:
This shit is torture. Tricks: len(num1) >= len(num2). ifOdd, append inf to end. Formula to calc index in arr2.
k = (numsToRight - numsToLeft + len(nums2) - 2) // 2. Getting 4 boundary numbers, if out of range, -inf or +inf depending.
If out of while loop, must be edge case when nums1 len == nums2 len. 

"""

def solve(nums1, nums2):

    if len(nums1) < len(nums2):
        return solve(nums2, nums1)
    # nums1 is longer, so pivot will be within nums1 range
    # Edge case, if nums1 == nums2 lengthwise, could go out of range of nums1

    isOdd = (len(nums1) + len(nums2)) % 2 == 1
    if (isOdd): nums1.append(float("inf")) # add dummy number to end to make calcs easier

    # setup binary search
    left = 0
    right = len(nums1) - 1

    while left <= right:
        pivot = left + (right - left) // 2 # bias left

        numsToLeft = pivot + 1
        numsToRight = len(nums1) - numsToLeft
        k = (numsToRight - numsToLeft + len(nums2) - 2) // 2 # should always be a whole number

        def getnum(idx, arr):
            if 0 <= idx and idx < len(arr):
                return arr[idx]
            elif idx < 0:
                return float('-inf')
            else:
                return float('inf')

        l1 = nums1[pivot] # always in range
        l2 = getnum(k, nums2)
        r1 = getnum(pivot + 1, nums1)
        r2 = getnum(k + 1, nums2)

        if l1 <= r1 and l1 <= r2 and l2 <= r1 and l2 <= r2: # found it
            if isOdd:
                return sorted([l1, l2, r1, r2])[1]
            else:
                arr = sorted([l1, l2, r1, r2])
                return (arr[1] + arr[2]) / 2
        elif l1 > r2: # l1 picked too far right.
            right = pivot - 1
        else: # l2 > r1, r1 too small, so pick more right
            left = pivot + 1
    
    return (nums2[-1] + nums1[0]) / 2

def solve(nums1, nums2):
    if len(nums1) < len(nums2):
        return solve(nums2, nums1)

    # now nums1 is longer, so split will always be in nums1
    # EDGE case: could be no elts of nums1 - check for this

    isOdd = (len(nums1) + len(nums2)) % 2 == 1

    # if odd, add a dummy number to end
    if (len(nums1) + len(nums2)) % 2 == 1:
        nums1.append(float("inf"))


    # setup binary search
    left = 0
    right = len(nums1) - 1

    while left <= right:
        pivot = left + (right - left) // 2 # bias left

        # Now we check the barrier numbers
        numsToLeft = pivot + 1
        numsToRight = len(nums1) - numsToLeft

        # Say arr2 index k. then k+1 nums to left and etc nums to right. need sums equal
        # numsToLeft + k + 1 = numsToRight + (len(nums2) - k - 1)
        # => 2k = numsToRight - numsToLeft + len(nums2) - 2
        # 1 2 3 4 5 inf
        # 6 7 

        k = (numsToRight - numsToLeft + len(nums2) - 2) // 2 # should be even?

        # so now perform checks
        # need 2 left values to be smaller or equal to 2 right values

        # EDGE CASE: end points?
        l1 = nums1[pivot]

        def getnum(idx, arr):
            if 0 <= idx and idx < len(arr):
                return arr[idx]
            elif idx < 0:
                return float('-inf')
            else:
                return float('inf')

        l2 = getnum(k, nums2)
        r1 = getnum(pivot + 1, nums1)
        r2 = getnum(k + 1, nums2)

        # print(l1, l2, r1, r2)

        if l1 <= r1 and l1 <= r2 and l2 <= r1 and l2 <= r2: # found it
            if isOdd:
                return sorted([l1, l2, r1, r2])[1]
            else:
                arr = sorted([l1, l2, r1, r2])
                return (arr[1] + arr[2]) / 2
        elif l1 > r2: # l1 picked too far right.
            right = pivot - 1
        else: # l2 > r1, r1 too small, so pick more right
            left = pivot + 1
    
    # Normal execution, returns from loop => will find if there is an idx nums1 that works.
    # Edge case, nums1 size == nums2 size.
    # and all nums in num1 > nums in num2, so off the grid
    # only happens with even nums since with odd, nums1 always greater
    assert(right == -1)
    return (nums2[-1] + nums1[0]) / 2


# print(solve([1, 2], [3, 4]))
# print(solve([1], [2]))
# print(solve([2], [1]))
# print(solve([1, 2, 3], [4, 5, 6]))
print(solve([1, 3, 4], [2, 5, 6]))
print(solve([1, 3, 4, 8], [2, 5, 6]))
print(solve([2, 2, 2], [3, 3, 4]))
print(solve([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17]))



        







