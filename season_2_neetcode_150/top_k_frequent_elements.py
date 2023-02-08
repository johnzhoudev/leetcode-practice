# Results:
# Runtime: 115ms 48.94%
# Memory Usage: 19.3MB 30.82%

"""

https://leetcode.com/problems/top-k-frequent-elements/

Given array nums, k
- return k most frequent elements

Ideas:
- find frequency, parse and add to dictionary - O(n)
- get k most frequent elements - sort? O(n log n), then return

- use heap, O(n) get frequency, then O(k log n) to get k most frequent elements

- load in k elements, keep track of min

- Technically, yeah, create array where frequency is index - then iterate - kind of like ad hoc bucket sort since we know max frequency

Tactic: frequencey easy, and bucket sort for top k. Max freq is len(n)

"""

def solve(nums, k):
    # find frequencies
    frequenciesMap = {}
    for num in nums:
        if num in frequenciesMap:
            frequenciesMap[num] += 1
        else:
            frequenciesMap[num] = 1
    
    # find k elements
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequenciesMap.items():
        buckets[freq].append(num)
    
    soln = []
    idx = len(nums)
    while (len(soln) < k):
        if len(buckets[idx]) != 0:
            soln.append(buckets[idx].pop())
        else:
            idx -= 1
    
    return soln
