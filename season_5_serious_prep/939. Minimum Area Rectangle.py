"""

939. Minimum Area Rectangle

array of points

return smallest rectangle area with these points, or 0

Rectangle => requires 2 y's and 2 x's, and points corresponding to those combinations

Idea:
- sort points by x value, then by y value (though 2nd sort by y doesn't really matter)
- if 2 x's the same...?

Or, make map from x value to points and y value to points

Honestly at this point maybe do brute force

Idea 2:
- create map from y value to x values with that y value
- Also create map from x value to y values of all points
- For each x value, take combos of y values and see if there are any such points 
with same y values later with same x value

- Given 2 points on same x, with different y's, take all points (x', y1) and see if final point exists

Time complexity
O(n) to add everything to maps
O(n^2) potential combos for one x 

Better idea: O(n^2) anyway, check all pairs of points and see if others exist too using a hashset

Tactic:
Just check all pairs of points and see if other corners are in too using set. Or, more complicated but make x to y map and y to x map and compare.

"""

def solve(points):
    pointsSet = set()
    for x, y in points:
        pointsSet.add((x, y))
    
    bestArea = float("inf")

    def dist(x, y):
        return abs(y - x)
    def area(x1, y1, x2, y2):
        return dist(x1, x2) * dist(y1, y2)

    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            if x1 == x2 or y1 == y2: continue

            if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                bestArea = min(bestArea, area(x1, y1, x2, y2))
    
    return bestArea if bestArea != float("inf") else 0

from collections import defaultdict

def solve(points):
    xValMap = defaultdict(list)
    yValMap = defaultdict(set) # set so can check existence easily

    def dist(x, y):
        return abs(y - x)
    def area(x1, y1, x2, y2):
        return dist(x1, x2) * dist(y1, y2)

    for x, y in points:
        xValMap[x].append(y)
        yValMap[y].add(x)
    
    bestArea = 0

    # Now brute force
    for x1 in xValMap:
        if len(xValMap[x1]) < 2: continue
        # Now try all combos

        yvals = xValMap[x1]
        for i in range(len(yvals)):
            for j in range(i + 1, len(yvals)):
                y1 = yvals[i]
                y2 = yvals[j]

                # For everything at height y1, is there anything at height y2 with same x?
                xvalsY1 = yValMap[y1]
                xvalsY2 = yValMap[y2]
                for x2 in xvalsY1:
                    if x2 <= x1: continue
                    if x2 in xvalsY2:
                        a = area(x1, y1, x2, y2)
                        bestArea = a if bestArea == 0 else min(bestArea, a)
    
    return bestArea



    
    