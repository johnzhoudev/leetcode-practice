"""

380. Insert Delete GetRandom O(1)

insert, remove, getRandom

Idea:

hash table of element to idx
list of elements
- swap with end and remove, and remove from hash table

wait, because hash table to index doesn't work. need to be to linked list node since indices change

O(1) for all operations

Finally.

Tactic:
swap elt with end and delete. Keep hash table of elt to index. Don't forget to update index in hash table after swap in remove!

"""

import random

class RandomizedSet:

    def __init__(self):
        self.elts = {}
        self.arr = [] # for random access

    def insert(self, val: int) -> bool:
        if val in self.elts: return False
        self.arr.append(val) # add to back
        self.elts[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elts: return False
        # set last to this element
        oldidx = self.elts[val]
        swappedVal = self.arr[-1]

        # do the swap
        self.arr[self.elts[val]] = self.arr[-1]
        self.elts[swappedVal] = oldidx

        self.arr.pop()
        del self.elts[val]

        # reset old swapped val idx to position
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)
