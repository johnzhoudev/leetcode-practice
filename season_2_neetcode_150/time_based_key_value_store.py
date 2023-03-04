# Results:
# Runtime: 755ms 76.16%
# Memory Usage: 71.6MB 66.67%

"""

https://leetcode.com/problems/time-based-key-value-store/

- store value with key and timestamp
- get with key and timestamp, choose most recent timestamp <= timestamp, or return ""

- binary search best since you need to find most recent - non-trivial in O(1)

IMPORTANT: timestamps inserted in ascending order

Idea:
- hash table for key, stores sorted list of timestamps
- insert? just append, O(1)
- retrieve, binary search, O(log n)

Tactic: take advantage of fact timestamps inserted in ascending order. hash table to timestamps, then binary search. If insert timestamp out of order, store as binary tree
Better: if inserting timestamps out of order, store as binary tree. then search, can traverse

"""

class TimeMap:

    def __init__(self):
        self.keyHash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyHash:
            self.keyHash[key] = []
        # assert(len(self.keyHash[key]) == 0 or self.keyHash[key][-1][0] < timestamp)
        self.keyHash[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyHash:
            return ""
        entries = self.keyHash[key]
        left = 0
        right = len(entries) - 1

        while left < right: # for this search, want to bias right. also keep left
            pivot = left + (right - left + 1) // 2  # bias right

            if entries[pivot][0] <= timestamp:
                left = pivot # keep as valid
            else:
                right = pivot - 1
        
        if entries[right][0] > timestamp:
            return ""
        return entries[right][1]



