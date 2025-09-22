"""

2349. Design a Number Container System

change(index, num)
find(num)

map of index to num
map of num to index? - set of indices
    - removing a num, how to get in order?

Then just take min from set of indices

O(1) time?
O(log n time)

    
tactic: heap and set, set tracks valid indices. pop invalids from heap when getting new min.
"""

import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index_set = {} # (min, heap of min, set of min)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            changed_num = self.index_to_num[index] # need to change

            # Fix other num
            indices_heap, indices_set = self.num_to_index_set[changed_num]

            # Remove fake mins
            indices_set.remove(index)
            while len(indices_heap) > 0 and indices_heap[0] not in indices_set:
                heapq.heappop(indices_heap)

            if len(indices_heap) == 0:
                del self.num_to_index_set[changed_num]

        # Add number
        self.index_to_num[index] = number

        # add other number to num set
        if number not in self.num_to_index_set:
            self.num_to_index_set[number] = ([], set())
        heap, index_set = self.num_to_index_set[number]
        index_set.add(index)
        heapq.heappush(heap, index)
        self.num_to_index_set[number] = (heap, index_set)

        # self.index_to_num[index] = number


    def find(self, number: int) -> int:
        if number not in self.num_to_index_set:
            return -1
        return self.num_to_index_set[number][0][0]



from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index_set = {} # (min, set of indices)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            changed_num = self.index_to_num[index] # need to change

            # Fix other num
            min_index, changed_num_indices = self.num_to_index_set[changed_num]
            changed_num_indices.remove(index)

            if len(changed_num_indices) == 0:
                del self.num_to_index_set[changed_num]
            else:
                if min_index == index:
                    min_index = min(changed_num_indices)
                self.num_to_index_set[changed_num] = (min_index, changed_num_indices)

        # Add number
        self.index_to_num[index] = number

        # add other number
        if number not in self.num_to_index_set:
            self.num_to_index_set[number] = (index, set())
        min_index, index_set = self.num_to_index_set[number]
        index_set.add(index)
        self.num_to_index_set[number] = (min(min_index, index), index_set)

        # self.index_to_num[index] = number


    def find(self, number: int) -> int:
        if number not in self.num_to_index_set:
            return -1
        return self.num_to_index_set[number][0]


cont = NumberContainers()
print(cont.change(2, 10))
print(cont.change(1, 10))
print(cont.change(3, 10))
print(cont.change(5, 10))
print(cont.find(10))