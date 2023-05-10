"""

https://leetcode.com/problems/hand-of-straights/

- arrange cards into groups where each group is size, and contains consecutive cards
- must match the group entirely

Ideas
- sort, then go in order to see if you can arrange. if you ever can't done.
- O(n log n)
- Otherwise for O(n), you would have to dynamically choose which group to add to. can't be done.
- unless super smart way

- Or, get min and max and make an array of values between and add nums
- then iterate thru, since all have to be consecutive
    - no, too many big values.

- hash table to linked list nodes in list, connected so you can traverse
- but can you traverse in order?

- count number of numbers you have, put in hash table
- then iterate thru in sorted order, since you want to add consecutively
    - so also sort, to some extent
    - because otherwise how to get min

Tactic: Store counts in hash table and loop thru from smallest numbers, and decrease counts. can use minheap or maybe just sort.

"""

from collections import defaultdict

def solve(hand, groupSize):
    # first make count of values
    count = defaultdict(lambda: 0)
    for num in hand:
        count[num] += 1
    
    sortedNums = sorted(list(set(hand)))

    for num in sortedNums:
        while count[num] > 0:
            numAdjacent = 0
            currNum = num # not included yet
            while numAdjacent < groupSize:
                if count[currNum] > 0:
                    numAdjacent += 1
                    count[currNum] -= 1
                    currNum += 1
                else:
                    return False # break, found a group without a consecutive thing
    
    return True

    