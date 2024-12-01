"""

670. Maximum Swap

num
can swap 2 digits at most once to get max value

return max value
basically want to swap leftmost digit with the largest thing afterwards

iterate thru digits backwards, track largest seen, and keep max value

Tactic:
Iterate backwards, track largest seen, anytime you see smaller digit, that's best to swap. only swap at end!

"""

def solve(num):

    numstr = [c for c in str(num)]
    largestSeen = -1
    largestSeenIdx = -1

    besti = -1
    bestj = -1

    def swap(i, j):
        temp = numstr[i]
        numstr[i] = numstr[j]
        numstr[j] = temp

    for i in range(len(numstr) - 1, -1, -1):

        # first try and swap
        if largestSeenIdx != -1 and int(numstr[i]) < largestSeen:
            # passed a digit
            # swap(i, largestSeenIdx)
            besti = i
            bestj = largestSeenIdx
            # swap(i, largestSeenIdx)

        if int(numstr[i]) > largestSeen:
            largestSeen = int(numstr[i])
            largestSeenIdx = i
    
    if besti != -1:
        swap(besti, bestj)
        return int(''.join(numstr))
    return num
        
print(solve(23))

        
