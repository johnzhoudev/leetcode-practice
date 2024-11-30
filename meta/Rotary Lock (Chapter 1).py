"""

num seconds to select m integers in order

- just naive way
- function to calc distance to number

c is list of numbers
n numbers on wheel
"""

def solve(n, m, c):

    def calcDistance(a, b):
        if a > b: return calcDistance(b, a)
        # a <= b
        return min(b - a, n - (b - a))

    last = 1
    numSeconds = 0
    for num in c:
        numSeconds += calcDistance(last, num)
        last = num
    
    return numSeconds



