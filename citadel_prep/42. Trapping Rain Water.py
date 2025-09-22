"""

42. Trapping Rain Water

2 pointer
- advance which one is smaller, keep track of largest left and largest right


"""

def solve(height):
    total = 0
    left = 0
    right = len(height) - 1
    largestLeft = height[left]
    largestRight = height[right]

    while left <= right:

        if height[left] < height[right]: # move left
            total += max(0, min(largestLeft, largestRight) - height[left])
            left += 1
            largestLeft = max(height[left], largestLeft)
        else:
            total += max(0, min(largestLeft, largestRight) - height[right])
            right -= 1
            largestRight = max(height[right], largestRight)
        
    return total



        
print(solve([0,1,0,2,1,0,1,3,2,1,2,1]))
    

