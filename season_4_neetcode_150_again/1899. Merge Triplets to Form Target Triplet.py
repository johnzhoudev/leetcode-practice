"""

triplets array
target trioplet

- to combine, choose 2 elemenets of triplets and take max of each field
- is it possible to combine to get target triplet?

Ideas:
- sort all of them and slowly take max?
- would work
- also filter out any that go over
O(n log n)

BETTER: Don't even sort! Just filter out all bad ones!
- because by applying all, you justget closer to answer but never over!
O(n)

Tactic:
DO NOT SORT! Filter out bad and combine! End result will be target, or not!

"""

def solve(triplets, target):
    # filter out all bads, and find max values for a b c
    t1, t2, t3 = target
    a, b, c = [float('-inf') for _ in range(3)]

    for a1, a2, a3 in triplets:
        if a1 > t1 or a2 > t2 or a3 > t3: continue
        a = max(a, a1)
        b = max(b, a2)
        c = max(c, a3)
        if a == target[0] and b == target[1] and c == target[2]: return True
    
    return False





def solve(triplets, target):
    def compare(trip1, trip2):
        for x, y in zip(trip1, trip2):
            if x == y: continue
            if x < y: return -1
            else: return 1
        return 0 # equal
    def merge(trip1, trip2):
        for i in range(len(trip1)):
            trip1[i] = max(trip1[i], trip2[i])

    def badTriplet(trip):
        for x, y in zip(trip, target):
            if x > y: return True
        return False
    
    curr = None

    for triplet in triplets:
        if badTriplet(triplet): continue
        if curr == None: curr = triplet
        else: merge(curr, triplet)

    return compare(curr, target) == 0 if curr else False



from functools import cmp_to_key

def solve(triplets, target):

    # - if < 0, 0, + if >
    def compare(trip1, trip2):
        for x, y in zip(trip1, trip2):
            if x == y: continue
            if x < y: return -1
            else: return 1
        return 0 # equal
    
    def merge(trip1, trip2):
        for i in range(len(trip1)):
            trip1[i] = max(trip1[i], trip2[i])

    def badTriplet(trip):
        for x, y in zip(trip, target):
            if x > y: return True
        return False
        
    triplets = [triplet for triplet in triplets if not badTriplet(triplet) ]
    if len(triplets) == 0: return False
    triplets = sorted(triplets, key=cmp_to_key(compare))

    curr = triplets[0].copy()
    for triplet in triplets:
        merge(curr, triplet)
        if compare(curr, target) == 0: return True
    return False




