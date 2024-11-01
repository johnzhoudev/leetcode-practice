"""

846. Hand of Straights

arrange cards into groups
size groupSize
groupsize consecutive cards

Idea:
- sort
- go thru and add
O(n log n)

- how to do without sorting?
- would have to know for each card which group to ad it too
    - hashing? hash +1 and -1
    - no idea how many cards, hard to update
    - resolving mdidle groups

    https://leetcode.com/problems/hand-of-straights/description/

Tactic:
count cards, sort, and for each non-zero-count card, try and add groupSize in helper func. Throw error if cannot 

"""

from collections import defaultdict
def solve(hand, groupSize):
    # get card counts
    cardCounts = defaultdict(lambda : 0)
    for card in hand:
        cardCounts[card] += 1
    
    hand = sorted(list(cardCounts))

    # should try and add groupSize cards, raise error if can't
    # updates card counts
    def tryAdd(card):
        groupCount = 0
        while groupCount < groupSize:
            if cardCounts[card] == 0: raise RuntimeError("Can't add card!")
            cardCounts[card] -= 1
            groupCount += 1
            card += 1

    # add all cards 
    for card in hand:
        while cardCounts[card] != 0:
            try: tryAdd(card)
            except RuntimeError: return False
    
    return True







solve([1, 2, 2, 3], 2)
        


