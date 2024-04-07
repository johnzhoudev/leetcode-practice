"""

https://leetcode.com/problems/flipping-an-image/description/

flip image horizontally and invert

- Flip using swap from both ends, like reversing a string

"""

def solve(img):
    n = len(img)

    for row in range(n):
        for i in range(n // 2): # floor divide, so skip middle
            temp = img[row][i]
            img[row][i] = 1 - img[row][n - i - 1]
            img[row][n-i-1] = 1 - temp
    

    # for row in range(n):
    #     for col in range(n):
    #         img[row][col] = 1 - img[row][col]
    
    return img