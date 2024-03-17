"""

373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

2 arr non decreasing order
int k

- return pairs distinct (one elt from 1st, from 2nd) with smallest sums

brute force: get sums of all pairs and sort and return

Greedy algorithm? 
- try to advance B, but if advancing A X

- maintain a pool? or heap? keep adding (A, b) and if have to incerease A, start at beginning of b
- that will be correct
- or every time you pop, add the next step? increase a or b?
O(k log k) (at most 2k elements in heap...?)

- CAREFUL - doesn't handle repeats?
- add a set

Note: This works!
Better: Notice that if list 1 has more than k elements, you'll never use the elts larger than the kth.
- this is because elts before + min elt from list 2 always smaller than the larger elts!
- So then it becomes a k way dixie cup merge sort from the first 1 elts in list 1

Tactic: k way merge on first k elts in list 1

"""

# minheap
from heapq import heappop, heappush

def solve(l1, l2, k):
    heap = [] # (size, idx1, idx2)
    added = set()

    def get_entry(idx1, idx2):
        return (l1[idx1] + l2[idx2], idx1, idx2)

    heappush(heap, get_entry(0, 0))
    added.add((0, 0))

    # begin loop
    output = []
    for _ in range(k):
        size, idx1, idx2 = heappop(heap)
        output.append((l1[idx1], l2[idx2]))

        # now add new ones
        if idx2 + 1 < len(l2) and (idx1, idx2 + 1) not in added:
            heappush(heap, get_entry(idx1, idx2 + 1))
            added.add((idx1, idx2 + 1))
        if idx1 + 1 < len(l1) and (idx1 + 1, idx2) not in added:
            heappush(heap, get_entry(idx1 + 1, idx2))
            added.add((idx1 + 1, idx2))

    return output
    

def solve2(l1, l2, k):
    heap = []

    def get_entry(idx1, idx2):
        return (l1[idx1] + l2[idx2], idx1, idx2)

    # init k way merge
    for i in range(min(len(l1), k)):
        heappush(heap, get_entry(i, 0))
    
    # do outpout
    output = []
    for _ in range(k):
        size, idx1, idx2 = heappop(heap)
        output.append((l1[idx1], l2[idx2]))

        if idx2 + 1 < len(l2):
            heappush(heap, get_entry(idx1, idx2 + 1))
    
    return output
        
