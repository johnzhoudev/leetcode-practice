"""


1762. Buildings With an Ocean View

n buildings in line
heights

all buildings to right have smaller heght

return index of buildings with ocean view in increasing order

Idea:

- iterate from right, keep track of largest building seen. If curr building larger, ocean view. 
Then reverse list at end

Tactic:
- iterate from right, keep track of largest seen. Reverse list at end

"""

def solve(heights):

    largest = 0
    cansee = []
    for i in range(len(heights) -1, -1, -1):
        if heights[i] > largest:
            cansee.append(i)
            largest = heights[i]
    
    return cansee[::-1]