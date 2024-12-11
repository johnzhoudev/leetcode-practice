"""

398. Random Pick Index

randomly output index of target num?

Idea:
- map of value to indices
- select random index

O(1) time to pick
O(n) time to setup
O(n) space

Other idea:
- reservoir sampling, first hat 1/1 chance to pick, second 1/2, third 1/3, ...
- do this for all hats, 

Say there's 4 hats
- last hat has 1/4 chance
- 2nd last hat has 1/3 * 3/4 = 1/4 chance
-...

Tactic:
Keep hash table of number to idx's. random.choice. Or, reservoir picking 1/1 for first hat, 1/2 for 2nd, 1/3...

"""

import random
from collections import defaultdict
# random.choice(list)


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        pick = -1
        for idx, num in enumerate(self.nums):
            if num != target: continue
            # Equal to target
            if random.randint(0, count) == 0:
                pick = idx
            count += 1
        
        return pick

class Solution:

    def __init__(self, nums):
        self.map = defaultdict(list)
        for idx, num in enumerate(nums):
            self.map[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])
        
