"""

https://leetcode.com/problems/search-a-2d-matrix/

binary search x, then y 
runtime log n + log m = log(nm)

"""

def solve(matrix, target):
    
    # how to access keys? - pass getter lambda
    def binarySearch(matrix, tar, get):
        left = 0
        right = len(matrix) # exclusive

        while left < right:
            


