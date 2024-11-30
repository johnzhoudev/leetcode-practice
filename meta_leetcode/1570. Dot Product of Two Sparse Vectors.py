"""

1570. Dot Product of Two Sparse Vectors

compute dot product

- mostly 0 

- store map of index to value
- just compare keys of smaller map

O(numkeys) size to store
O(smaller map) to compute

Tactic:
Store map of index to value, and iterate thru smaller map to calc dot prod.

"""

class SparseVector:
    def __init__(self, nums):
        self.map = {}
        for i, num in enumerate(nums):
            if num == 0: continue
            self.map[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        if (len(self.map) > len(vec.map)):
            return vec.dotProduct(self)
        
        total = 0
        for key, value in self.map.items():
            if key in vec.map:
                total += (value * vec.map[key])
        
        return total
    

