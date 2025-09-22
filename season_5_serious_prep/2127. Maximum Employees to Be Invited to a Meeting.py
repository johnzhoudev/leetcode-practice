"""

2127. Maximum Employees to Be Invited to a Meeting

circular table
employees have favourites
fav is not themselves

max num employees that can be seated?

isn't it kind of like a chain
- ie, pick 1 person. then adjacent to them must seat another, then another, etc.
    - but must end with 1st diner OR prev?
    but it's a fixed chain
    so worst case, try all chains, O(n^2) time
    acc more complicated, right?

Is this some DP thing?
- dp[i] = max diners with i at end, using prev
    - doesn't work cuz depends on random other

Turn to graph?
- graph of needs
- can fit either cycle, or chain ending with self referencing

- just find longest cycle / self-referencing chains added together

- self-referncing chain - just do search from all no indegree, see if any.

search from no indegree. everything else must be a cycle, it's own cycle.

Either largest loop, or chains
    - keep dict of chain ends

"""

"""

Alg:
- Best seating arrangement is either
1. Largest loop of len > 2
2. Sum of all "chains", where chains end in a loop of len 2. Can stack multiple chains together (though some chains may end the 
same but have diff starting lengths)


"""

from collections import defaultdict

def solve(fav):

    # first identify nodes of no indegree
    no_indegree = set(range(len(fav)))
    for x in fav:
        if x in no_indegree: no_indegree.remove(x)
    
    # do search from nodes with no indegree
    # maintain loopcount to figure out length of loop
    chains = defaultdict(lambda: 0)
    bestLoopSize = 0

    # visited is map to timestamp of visited
    # Cache? if chain, return chain size. else return none => loop, already added.
    # also could have loops of size 2 that count as chains

    isALoop = set()
    chainCache = {} # if node is in a chain, returns (length of chain, ending node)

    # return None if loop, or chain size and ending node if chain
    def dfs(node, visited, timestamp):
        nonlocal chains
        nonlocal bestLoopSize

        #print(node, chains)
        #print(isALoop, chainCache)

        # check cache
        if node in isALoop:
            return None
        elif node in chainCache:
            chainLen, endNode = chainCache[node]
            return (chainLen, endNode)

        if node in visited:

            # wrap around to last node
            if visited[node] == timestamp - 2:
                # chains[fav[node]] = max(chains[fav[node]], timestamp) # take best
                chains[node] = max(chains[node], 2)

                return (0, fav[node]) # size and ending node

            else: # must be 
                loopSize = timestamp - visited[node]
                bestLoopSize = max(bestLoopSize, loopSize)

                if loopSize == 2: # a chain ending
                    # Check both ends
                    chains[node] = max(chains[node], 2)
                    chains[fav[node]] = max(chains[fav[node]], 2)

                    return (0, fav[node])

                else:
                    return None # loop

        # else explore
        visited[node] = timestamp
        res = dfs(fav[node], visited, timestamp + 1)
        del visited[node]

        # caching
        if res is None:
            isALoop.add(node)
            return None
        else:
            chainLen, endNode = res
            #print(chainLen, endNode, node, max(chainLen + 1, 2))

            # edge case for last node
            if chainLen == 0:
                assert(node == endNode)
                chainCache[node] = (2, fav[node])
                return (chainLen + 1, endNode)

            chainCache[node] = (chainLen + 1, endNode)
            chains[endNode] = max(chains[endNode], chainLen + 1)
            return (chainLen + 1, endNode)

    rest = set(range(len(fav)))
    for start in no_indegree:
        #print("IOndegree start", start)
        dfs(start, {}, 0)
        #print("chains", chains)
        #print("chaincache", chainCache)
        rest.remove(start)
    for x in rest:
        #print("rest start", x)
        dfs(x, {}, 0)
    
    chainTotal = 0
    for node in chains:
        chainTotal += chains[node] + chains[fav[node]] - 2
    chainTotal //= 2

    #print(no_indegree)
    #print(isALoop)
    #print(chains, chainTotal)
    #print(bestLoopSize)
    return max(chainTotal, bestLoopSize)


    
# #print(solve([1,0,0,2,1,4,7,8,9,6,7,10,8]))
#print(solve([2,2,1,2]))
    
