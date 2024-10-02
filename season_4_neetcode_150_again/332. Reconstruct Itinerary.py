"""

332. Reconstruct Itinerary

- from, to
- all depart from jfk
- return smallest lexicographical ordering
- must use all tickets?

- basic graph puzzle?
- just do dfs? prioritize smaller lexicographical airport?
- greedy? just take smallest lexicographical from each airport?
    - could run into dead end without hitting all others
    - so do dfs and pick lowest lexical, but go in order

- if a search reaches the end, return that ordering
    - continue search

Idea:
- greedy search till end
- on return, if any unused, continue search for loops and continue

Time: O(n) - only reached once
Space: O(n^2) for adj list?

BETTER: Eulerian Path Algorithm

Tactic: DFS to explore all the way. Then if stuck, at end. So pop and write down node

Tactic: 
Sort adj lists in reverse and pop to explore during dfs. Do dfs from JFK, and when no more moves, append curr to path. Reverse path at end.

"""

def solve(tickets):
    # Eulerian path alg
    # adj list
    adjList = defaultdict(list)
    for fr, to in tickets:
        adjList[fr].append(to)
    
    for key in adjList:
        adjList[key].sort(reverse=True) # pop so u can go in inc order
    
    path = []

    def dfs(curr):
        # if dead end, show
        # Try to explore using adjList
        while adjList[curr]:
            next = adjList[curr].pop()
            dfs(next)
        path.append(curr)
    
    dfs('JFK')
    return path[::-1]


from collections import defaultdict
def solve(tickets):

    adjList = defaultdict(list)
    unusedTickets = defaultdict(lambda : 0) # key is fr, to

    for fr, to in tickets:
        adjList[fr].append(to)
        unusedTickets[(fr, to)] += 1
    
    for key in adjList:
        adjList[key].sort() # make alphabetical
    

    # Now do dfs

    def dfs(curr, adjList):

        # Check if reached dead end 
        isFinished = True
        for dest in adjList[curr]:
            if unusedTickets[(curr, dest)] != 0:
                isFinished = False
                break
        
        if isFinished:
            return [curr]
        
        # Mark as visited
        
        # Explore next
        toEnd = []

        # First time it returns, must be to the end
        for dest in adjList[curr]: # sorted
            if unusedTickets[(curr, dest)] > 0:
                unusedTickets[(curr, dest)] -= 1
                # Will only return with the finished path
                if len(toEnd) == 0:
                    toEnd = dfs(dest, adjList)
                else:
                    res = dfs(dest, adjList)
                    toEnd = res + toEnd # extend
        
        return [curr] + toEnd
    
    return dfs("JFK", adjList)

        
# test cases
print(solve([["JFK", "ABC"], ["ABC", "MTR"], ["MTR", "ABC"], ["ABC", "AYZ"]]))



