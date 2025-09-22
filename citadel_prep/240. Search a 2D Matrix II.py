"""

240. Search a 2D Matrix II

rows sorted left to right
cols sorted top to bottom

Binary search on rows to find r ows to search

omg start at top right. If target > num, cannot be in whole row. if target < num, cannot be in col. narrow down.

"""

def solve(matrix, target):
    r, c = 0, len(matrix[0]) - 1 # top right

    def inbounds(r, c):
        return 0 <= r and r < len(matrix) and 0 <= c and c < len(matrix[0])
    
    while inbounds(r, c):
        pivot = matrix[r][c]
        if target > pivot: # cannot be in row
            r += 1
        elif target < pivot: # cannot be in col
            c -= 1
        else:
            return True
    
    return False


