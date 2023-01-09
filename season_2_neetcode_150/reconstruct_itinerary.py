# Results:
# Runtime: 82ms 91.11%
# Memory Usage: 14.1MB 99.65%

"""

https://leetcode.com/problems/reconstruct-itinerary/

Ideas:
- construct a graph of all the tickets, then do a dfs? must be able to go thru all
    - store graph as a hash table, hashing city to city - adjacency list
    - if you find one that has smaller lexicographical order and is valid, return?
        - just do comparison operators, <, >, =

- Math trick: you need to use all edges, so other than main path, will just have loops
    - do dfs to reach
    - if not at destination and can still go, choose lowest cost thing until you reach dest
    - then will have path, and only loops left
    - as you pop and add to result, keep trying to traverse but since backwards, get highest

Tactic: math trick, you must use all the edges so departures from a main route are loops. So from a main route, 
just take lowest val route to get optimal. All edges must be travelled so just take min one and you should end up at dest
Also do dfs with while loop to keep going until you can't. Then pop from stack, this is the route.
"""

def solve2(tickets):
    # construct graph
    graph = {}
    for origin, dest in tickets:
        if origin in graph:
            graph[origin] += [dest]
        else:
            graph[origin] = [dest]
    
    # sort dests
    for origin in graph:
        graph[origin].sort(reverse=True) # sort Descending, so when we pop from back, we get smallest
    
    # do dfs all the way, then when you pop, see if you can still go
    stack = ["JFK"]
    result = []

    while stack:

        while stack[-1] in graph and graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop()) # take the smallest first

            # if this is a loop, this will take us thru all the loops, where largest at back
        
        # once reached dead end, must be at end. so pop result and add to front of route
        result.insert(0, stack.pop())

    return result



    
    

# tickets is a list of two-pair of strings, from to dests
def solve(tickets):
    # construct graph
    numTickets = 0
    graph = {}
    for idx, (origin, dest) in enumerate(tickets):
        if origin in graph:
            graph[origin] += [(dest, idx)]
        else:
            graph[origin] = [(dest, idx)]
        numTickets += 1
    
    # DFS to generate solutions, but do it using edges. can revisit nodes, but have to use edges
    # need visited set to track where we've been
    # JFK will always be starting point

    toProcess = [(None, "JFK", -1)]
    ticketsUsed = set() # set of from and to pairs
    lowestResult = []
    lowestResultStr = ""
    currentResult = []

    while len(toProcess) != 0:
        origin, dest, idx = toProcess.pop()

        # first time seeing, so push back on
        if (origin, dest, idx) not in ticketsUsed:
            toProcess.append((origin, dest, idx))
        else:
            # second time seen, so pop from currentResult
            currentResult.pop() # popping 
            ticketsUsed.remove((origin, dest, idx))
            continue

        # haven't visited node yet
        if (origin, dest, idx) in ticketsUsed:
            print("Error, should never get here")
            continue
            
        ticketsUsed.add((origin, dest, idx))

        # process node
        currentResult += [dest]

        # add children
        end = True
        if dest in graph:
            for nextDest, nextIdx in graph[dest]:
                if (dest, nextDest, nextIdx) not in ticketsUsed:
                    toProcess.append((dest, nextDest, nextIdx))
                    end = False
        
        # no more valid next dests, and used up all tickets
        if (end and len(currentResult) == numTickets + 1):
            currentResultStr = ""
            for s in currentResult: currentResultStr += s
            if lowestResultStr == "" or currentResultStr < lowestResultStr:
                lowestResult = currentResult.copy()
                lowestResultStr = currentResultStr
        
    return lowestResult



