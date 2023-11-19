# Shrinkable Sliding window
# classic sliding window

def invalid():
    pass
def valid():
    pass

def slide(arr):
    left = 0
    right = 0 # inclusive
    maxSize = 1
    while left <= right and right <= len(arr):

        while left <= right and not invalid():
            left += 1 # shrink

        if valid():
            maxSize = max(maxSize, right - left + 1)

        right += 1 # expand
    return maxSize

# Non-shrinking sliding window
# if looking for max size, each time either extend, or shift. Since don't need to consider smaller
# see Frequency of most frequent element

# Binary Search Type Questions
# - KOKO eating bananas, binary search on sorted elts and verify in O(n) time
# - Longest increasing subsequence - binary search on sizes!!!
# - otherwise should be straightforward
        
