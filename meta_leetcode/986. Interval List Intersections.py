"""

986. Interval List Intersections

sorted list
pairwise disjoint

return intersection of the 2 intervals

when comparing 2 intervals
- either 1 is before completely
    - pop the smaller one further to the left
- or overlapping
    - overlapped region is max(left1, left2) to min(right1, right2)
    - then pop the one that's further to the left

Tactic: 
check if overlap. if yes, left = max(lefts) and right=min(rights), then pop smaller right

"""

def solve(l1, l2):

    i1 = 0
    i2 = 0 # other index

    output = []

    while i1 < len(l1) and i2 < len(l2):

        left1, right1 = l1[i1]
        left2, right2 = l2[i2]

        # no overlap, 1 is left of 2
        if right1 < left2:
            i1 += 1
        elif right2 < left1: # 2 is to the left of 1
            i2 += 1
        else: # have overlap
            overlapLeft = max(left1, left2)
            overlapRight = min(right1, right2)
            output.append((overlapLeft, overlapRight))

            # figure out which to pop
            # want to pop the one with the smaller right border
            if right1 <= right2:
                i1 += 1
            else:
                i2 += 1
    return output
        
print(solve([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
