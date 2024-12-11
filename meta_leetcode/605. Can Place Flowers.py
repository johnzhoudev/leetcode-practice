"""

605. Can Place Flowers

true if n flowers can be planted without violating no adj rule or not

Greedy?

Do a scan and plant
- check next and previous


Tactic:
Simple scan. Beware of edge cases when n <= 0 from the start.

"""

def solve(flowerbed, n):

    def inRange(i):
        return 0 <= i and i < len(flowerbed)

    def canPlant(i):
        prev = i-1
        next = i+1
        if flowerbed[i] == 1: return False # occupied
        return (not inRange(prev) or flowerbed[prev] == 0) and (not inRange(next) or flowerbed[next] == 0)

    for idx, val in enumerate(flowerbed):
        if canPlant(idx):
            flowerbed[idx] = 1
            n -= 1
            if n <= 0: return True
    
    return n <= 0


