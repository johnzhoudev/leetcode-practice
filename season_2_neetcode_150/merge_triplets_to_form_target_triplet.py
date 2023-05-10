"""

https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

triplet - arr 3 ints
- array of triplets
- target = [x y z]

- operations
- 2 triplets, [max(ab)]

Ideas:
- get max item in triplet
- then second largest, union with that (requires first item less)
- then get third

- Actually, have to find 3 triplets where the 3 things are the max elts for each column. If they weren't, we would end up with an override.

- Do 3 passes
- first pass, find target with 1st and values less for 2nd and 3rd
- 2nd pass, find target with 2nd and values less for 1st and 3rd
- yada yada yada
- if can find all 3, done

Tactic: equivalent to finding 3 triplets where idx matches, and others are less than target. Make checkValid helper taking index, and just go thru.

"""

def solve(triplets, target):

    # idx to find, 0 1 2
    def checkValid(idx, triplet):
        for i in range(3):
            if i == idx and target[i] != triplet[i]:
                return False
            if i != idx and target[i] < triplet[i]:
                return False
        return True

    numFound = 0
    found = [False, False, False]
    for triplet in triplets:
        for i in range(3):
            if not found[i] and checkValid(i, triplet):
                numFound += 1
                found[i] = True
        if numFound == 3:
            return True
    return False
            


        



