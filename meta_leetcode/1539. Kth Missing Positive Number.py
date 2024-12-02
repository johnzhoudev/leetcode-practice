"""

1539. Kth Missing Positive Number

Idea:
positive integers are 1, 2, 3, ...
no duplicates

at index i, should be i+1 integers there.
- 

index 5, should be 6.
- but if it's 9, then we know the 5 numbers before it, all must be unique
    - but 9 - 6 = 3 numbers are missing

Binary search!

- now if missing == k, but previous number is value - 1, then go left as well

Tactic:
Sooo fucking confusing. But can calculate missing. After binary search, left index will be at value with missing < k. And right index
will be >= k. So missing number is arr[left] + k - (number of missing numbers to left of left) = k + right...???

"""

def solve(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = left + (right - left) // 2
        missing = arr[pivot] - (pivot + 1)
        if missing < k:
            left = pivot + 1
        else:
            right = pivot - 1
    
    # at end of loop, left = right + 1
    # we must have that right, number missing is < k
    # must also have that at left, number missing >= k
    # so missing number is between arr[right] and arr[left]
    # so return arr[right] (which has k-1 missing numbers)
    """
    missing numbers to left of arr[right] + valid numbers to right of arr[right] = arr[right]
    arr[right] + k - (missing numbers to left of arr[right])
    = arr[right] + k - (arr[right] - (right + 1))

    
    """
    return k - (right + 1)



def solve(arr, k):
    left = 0
    right = len(arr) - 1

    while left < right:
        pivot = left + (right - left) // 2 # bias left
        # figure out how many are missing
        missing = arr[pivot] - (pivot + 1)

        if missing < k: # go right
            left = pivot + 1
        else: # haven't found hte missing value yet
            right = pivot
        
    # at this point, we have narrowed down to an element
    # this element is either going to have missing more than k (and our k is below), or it's larger
    # everything to the left of it must have less missing

    missing = arr[left] - (left + 1)
    # missing number is len(array) + k, since kth missing number is beyond the array
    if missing < k: # then missing kth must be more than array
        return left + 1 + k # number of values including left, plus k
    else: # missing >= k
        # we are at the value for which missing >= k, and missing < k for the previous one
        # so, we must return previous 
        return left + k


print(solve([2,3,4,7,11], 5))
