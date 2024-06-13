"""

https://leetcode.com/problems/partition-equal-subset-sum/description/

partition into equal subsets

Brute force: get all subsets, test neg

- equivalent to finding if subset of numbs sunm to a number

Tactic: Find if subset can sum to half of the thing. Then keep a reachable sums set and go thru nums

"""

def solve(nums):
    total = sum(nums)
    if total % 2 == 1: return False
    target = total // 2

    reachableSums = set()
    reachableSums.add(0)
    for num in nums:
        nextSums = []
        for partialSum in reachableSums:
            if num + partialSum == target:
                return True
            if num + partialSum not in reachableSums and num + partialSum < target:
                nextSums.append(num + partialSum)
        
        for partialSum in nextSums:
            reachableSums.add(partialSum)
    return False
    




