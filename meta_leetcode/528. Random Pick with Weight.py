"""

528. Random Pick with Weight

w[i] = weight of ith index

randomly pick index
probability is weight[i] / sum

Idea:
- have array of index -> cumulative weight
- go to right weight given any number
- prng
- then just do a binary search to figure out your weight

O(log n) for each random gen
O(n) memory space, not O(weight sum). So better memory

Tactic:
Range of weights, binary search.

"""

import random

class Solution:

    def __init__(self, w):
        self.weights = []
        cumweight = 0
        for weight in w:
            cumweight += weight
            self.weights.append(cumweight)
        self.totalWeight = cumweight

    def pickIndex(self) -> int:
        
        # Do a binary search on totalweights. Want to find smallest index that's larger or equal
        target = random.randint(1, self.totalWeight)

        left = 0
        right = len(self.weights) - 1
        while left < right:
            pivot = left + (right - left) // 2 # bias left - because we keep larger
            val = self.weights[pivot]

            if val < target:
                left = pivot + 1
            else:
                right = pivot
        
        assert(left == right)
        return left



