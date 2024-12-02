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

"""

def solve(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = left + (right - left) // 2 # bias left


        # figure out how many are missing
        missing = arr[pivot] - (pivot + 1)

        print(pivot, arr[pivot], missing)

        if missing < k: # go right
            print("r")
            left = pivot + 1
        elif missing > k or missing == k and arr[pivot - 1] == arr[pivot] - 1: # haven't found hte missing value yet
            print('l')
            right = pivot
        else:
            assert(missing == k)
            return arr[pivot] - 1
        
    # at this point, didn't find. so just return k
    return k
    
    

print(solve([2,3,4,7,11], 5))
