# Results:
# Runtime: 36ms 97.97%
# Memory Usage: 14.4MB 82.35%

"""

https://leetcode.com/problems/search-a-2d-matrix/

binary search x, then y 
runtime log n + log m = log(nm)

- First search is going to narrow down on one element

Better:
- Treat as regular array, using modulo to get rows

Tactic: Treat as regular array, and use modulo magic

"""

def solve2(matrix, target):
    left = 0
    right = len(matrix) * len(matrix[0]) # exclusive

    while left < right:
        pivot = left + (right - left) // 2
        pivotElt = matrix[pivot // len(matrix[0])][pivot % len(matrix[0])]
        if target < pivotElt:
            right = pivot
        elif target > pivotElt:
            left = pivot + 1
        else:
            return True # found
    return False


def solve(m, tar):
    
    # how to access keys? - pass getter lambda
    def binarySearch(matrix, target, get):
        left = 0
        right = len(matrix) # exclusive
        pivot = -1

        while left < right:
            pivot = left + ((right - left) // 2) # biases to the right

            if get(pivot) < target: # go right
                left = pivot + 1
            elif get(pivot) > target:
                right = pivot
            else:
                return pivot

        # check direction on pivot, always return smaller
        if get(pivot) > target:
            return pivot - 1
        else:
            return pivot
    
    # first binary search on first elts
    row = binarySearch(m, tar, lambda x : m[x][0])
    col = binarySearch(m[row], tar, lambda x : m[row][x])
    return m[row][col] == tar





            


