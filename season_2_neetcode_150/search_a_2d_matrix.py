"""

https://leetcode.com/problems/search-a-2d-matrix/

binary search x, then y 
runtime log n + log m = log(nm)

- First search is going to narrow down on one element

"""

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





            


