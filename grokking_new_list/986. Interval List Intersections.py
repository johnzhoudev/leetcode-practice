"""

first list, second list, pairwise disjoint and sorted

return intersection of the two intervals


Idea:

- greedy, no?
- check if there's any overlap with the intervals
    - whichever one ends first, check if overlap with other. if yes, add. else, pop.
    - check start of other. if after, none. else figure it out
- pop intervals, whichever one ends first

- go thru once more and merge ones with same start and end - necessary if pairwise disjoint?

- O(n)

Tactic: Go thru, check overlap. 
Pro Tip: take max of left bound and min of right bound to get overlap, and if valid, add. then pop last.


"""

# f1, f2 assumed to be interval that ends first
def getOverlap(f1, f2, s1, s2):
    if s1 > f2:
        return None
    elif f1 <= s1:
        return [s1, f2]
    else:
        return [f1, f2]

def solve(firstList, secondList):
    soln = []
    firstList.reverse()
    secondList.reverse()

    # if any one is missing, break since no possible intersection
    while firstList and secondList:
        [f1, f2] = firstList[-1] # since reversed for ease of popping
        [s1, s2] = secondList[-1]

        firstEndsFirst = True
        if not f2 <= s2:
            firstEndsFirst = False
        
        if firstEndsFirst:
            overlap = getOverlap(f1, f2, s1, s2)
            if overlap is not None: soln.append(overlap)
            firstList.pop()
        else:
            overlap = getOverlap(s1, s2, f1, f2)
            if overlap is not None: soln.append(overlap)
            secondList.pop()
        
    return soln

