"""

88. Merge Sorted Array

sort non decreasing

merge into nums1

Idea:
- move all nums1 to back
- then merge

Better:
- Don't even need the copy, just merge backwards! will never overlap!

Tactic:
Don't even need the copy, just merge backwards! will never overlap!


"""

def solve(nums1, m, nums2, n):

    i = len(nums1) - 1
    i1 = m - 1
    i2 = n - 1

    while i1 >= 0 or i2 >= 0:

        if i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
        elif i1 >= 0:
            nums1[i] = nums1[i1]
            i1 -= 1
        else:
            nums1[i] = nums2[i2]
            i2 -= 1

        i -= 1
    
    return




def solve(nums1, nums2, m, n):

    # first move nums1 to back of nums1 array
    for i in range(m-1, -1, -1):
        nums1[i + n] = nums1[i]
    
    # merge
    i1 = m + n - m
    i2 = 0
    i = 0

    while i1 < len(nums1) or i2 < len(nums2):
        print(nums1)

        if i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
        elif i1 < len(nums1): # copy rest of i1
            nums1[i] = nums1[i1]
            i1 += 1
        else:
            nums1[i] = nums2[i2]
            i2 += 1

        i += 1
    
    print(nums1)
    return


solve([1,2,3,0,0,0], [2,5,6], 3, 3)
    


