"""

https://leetcode.com/problems/detect-squares/

add new points in xy plane
duplicate points allowed
given query point, count ways to choose 3 other points s.t. axis lingned square w/ positive area

0 \leq x ,y \leq 1000

at most 3000 adds in total

if given point, pick arbitrary 2nd point as diagonal (cannot be aligned) and confirm existence of 3rd and 4th points

Idea:

- use hash table for points x and y (confirm existence) (have count)
- Also include unique list of all points to iterate thru 
- multiply num points together to add to count

SQUARE! not rectangle

Tip: Use hash table / defaultdict instead of 2d array

Tactic: 


"""

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.pointCounts = defaultdict(lambda: 0)
        self.points = set()
        
    def add(self, point) -> None:
        # self.pointCounts[point[0]][point[1]] += 1
        self.pointCounts[tuple(point)] += 1
        self.points.add(tuple(point))

    def count(self, point) -> int:
        x = point[0]
        y = point[1]

        numWays = 0

        # for each unique point without shared x or y, check if can form diagonal
        for x2, y2 in self.points:
            if x2 == x or y2 == y or abs(x - x2) != abs(y - y2):
                continue
            numWays += self.pointCounts[(x, y2)] * self.pointCounts[(x2, y2)] * self.pointCounts[(x2, y)]
        
        return numWays


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)