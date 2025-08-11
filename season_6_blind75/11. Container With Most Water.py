"""

11. Container With Most Water

go from edges, greedy, increase the smaller one?
O(n)

Tacitc: Largest, go inwards by smaller edge and take max area
"""

def solve(heights):
    left = 0
    right = len(heights) - 1
    best = 0

    while left < right:
        l_height = heights[left]
        r_height = heights[right]

        rect_height = min(l_height, r_height)
        area = (right - left) * rect_height

        best = max(area, best)

        if l_height < r_height:
            left += 1
        else:
            right -= 1
    
    return best



