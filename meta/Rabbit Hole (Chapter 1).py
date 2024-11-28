"""

Rabbit Hole (Chapter 1)

n webpages
page i has 1 link to another page

max number of pages you can visit if can start on 1 page?

Directed graph

dfs from each component

say you pick v, dfs means picking any would be as good as picking v
- so only do dfs from ones you haven't seen
O(n)

- Each time you dfs, you count the number of nodes not seen by the other search
    - if more?

- can't really save state from one dfs pass

O(n^2) worst case, do dfs from nodes not picked by traversal

Wait, only 1 link per page
- can follow until a loop
    - CAN calculate for each node how long the access is

- once find loop, how to return?

- store hash map of node and num steps
    - once reach loop, can figure out length of loop from that
- can deduce size of loop
- complicated to set on recursion the reachable


Maybe 2 phases
- follow until loop
- then from loop, follow and set all
- then from everything before, set

O(n) time

Tactic:


"""

def solve(N, links):

    state = {}
    links = [-1] + links

    visited = set()

    # goes thru and once finds loop, sets state for all elements in loop 
    def setLoop(i):
        stack = [i]
        curr = links[i]
        while curr != i:
            stack.append(curr)
            curr = links[curr]
        
        # now at loop
        loopLen = len(stack)
        while stack:
            val = stack.pop()
            state[val] = loopLen
        
        return loopLen

    def follow(i):
        if i in state: return state[i]

        # if loop
        if i in visited:
            setLoop(i) # returns the loop len
            return 0
        
        visited.add(i)
        res = 1 + follow(links[i]) # counts backwards thru stack

        if i not in state: # if not already set by setLoop
            state[i] = res

        return res
    
    best = -1
    for i in range(1, N + 1):
        print(i)
        best = max(follow(i), best)
        visited.clear()
    return best

def solve2(N, links):

    state = {}
    links = [-1] + links

    visited = set()

    # goes thru and once finds loop, sets state for all elements in loop 
    def setLoop(i):
        stack = [i]
        curr = links[i]
        while curr != i:
            stack.append(curr)
            curr = links[curr]
        
        # now at loop
        loopLen = len(stack)
        while stack:
            val = stack.pop()
            state[val] = loopLen
        
        return loopLen

    def follow(i):
        stack = [i]

        res = -1

        while stack:
            val = stack.pop()

            if val in state:
                res = state[val]
                break

            # if loop
            if i in visited:
                setLoop(i) # returns the loop len
                res = 0
                break
            
            visited.add(i)
            stack.append(i)
            stack.append(links[i])
        
        # walk backwards thru stack, get rid of stuff
        assert(res >= 0)
        while stack:
            val = stack.pop()

            if val not in state: # if not already set by setLoop
                state[val] = res + 1
            res += 1
        
        return state[i]
    
    best = -1
    for i in range(1, N + 1):
        best = max(follow(i), best)
        visited.clear()
    return best


def solve(N, links):
    # Must do everything iteratively
    state = {}
    links = [-1] + links

    def search(page):
        instack = {} # map page to pathlen
        stack = [] # holds page, pathlen
        time = 0

        # haven't seen page, and not loop
        while page not in instack and page not in state:
            stack.append((page, time))
            instack[page] = time
            time += 1
            page = links[page]
        
        # either reached found page, or loop
        # if loop

        steps = -1

        if page in instack: # loop
            prevpage, prevtime = stack.pop()
            pagetime = instack[page]

            # now calculate
            loopsize = prevtime - pagetime + 1

            # for rest of things in loop, set
            while prevpage != page:
                state[prevpage] = loopsize
                prevpage, _ = stack.pop()
            state[page] = loopsize
            steps = loopsize
        else:
            steps = state[page]

        while stack:
            page, _ = stack.pop()
            steps += 1
            state[page] = steps
        
        return steps
    
    best = -1
    for i in range(1, N+1):
        best = max(search(i), best)
    
    return best


N = 7
links = [2, 1, 1, 1, 1, 1, 1]

print(solve(N, links))

x = [1, 2, 3]
x = [-1] + x
print(x)