"""

935. Knight Dialer

- make graph?
- edges between adjacent values

- to get combos, do dfs?

Everyone can jump to 2, with exception 4 and 6 who can jump to 3
    - can be reached from 3 places

    search alg?

if from reg num, *2 *2
if from 4 or 6, *2 *3


DP:
- for each num, keep track of num ways gotten to it so far
- everyone starts off at 1, and each iter, add it up


Tactic:
Keep track of all ways to reach numbers, and each iter, add those up.

"""

def solve(n):
    nextElt = [None for _ in range(10)]
    nextElt[0] = [4, 6]
    nextElt[1] = [6, 8]
    nextElt[2] = [7, 9]
    nextElt[3] = [4, 8]
    nextElt[4] = [0, 3, 9]
    nextElt[5] = []
    nextElt[6] = [0, 1, 7]
    nextElt[7] = [2, 6]
    nextElt[8] = [1, 3]
    nextElt[9] = [2, 4]

    counts = [1 for _ in range(10)]

    for i in range(1, n):
        newCounts = [0 for _ in range(10)]
        for i in range(10):
            if i == 5: continue
            for k in nextElt[i]:
                newCounts[k] += counts[i] % (10**9 + 7)
        counts = newCounts
    
    return sum(counts) % (10**9 + 7)




def solve(n):

    nextElt = [None for _ in range(10)]
    nextElt[0] = [4, 6]
    nextElt[1] = [6, 8]
    nextElt[2] = [7, 9]
    nextElt[3] = [4, 8]
    nextElt[4] = [0, 3, 9]
    nextElt[5] = []
    nextElt[6] = [0, 1, 7]
    nextElt[7] = [2, 6]
    nextElt[8] = [1, 3]
    nextElt[9] = [2, 4]

    total = 0
    for start in range(10):
        if start == 5: continue
        stack = [(1,start)]
        while stack:
            l, curr = stack.pop()

            if l == n:
                total = (total + 1) % (10**9 + 7)
                # stop exploring
            else:
                # continue exploring
                for k in nextElt[curr]:
                    stack.append((l + 1, k))
        
    return total

print(solve(2))

            



