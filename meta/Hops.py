"""

n lillypads
f frogs
frog i is perched upon lilipad p[i]
- no 2 frogs on same pad
- no frogs on lilipad n

frog hops over all frogs to next available lilipad
- if lands on pad n, done

- last frog should always hop, since if it doesn't then it'll incur extra hops regardless
- should just be greedy, last frog always hops?

- how to calculate fast?

not frogs hopping, but groups moving together shifting 1 forward at a time
- when connect, become bigger fleet


- Sort frogs on pads
- last frog moves forward until 2nd last frog, then group, then continue moving forwards
until end
- then squeeze all out

Tactic:
Greedy, last frog just hops. Think about it like moving masses, joining with next until end

"""

def solve(n, f, p):
    p.sort()

    headFrog = p[0] # on lilipad 

    def dist(f1, f2): # hops for f1 to get to just behind f2
        if f1 == f2: return 0 # for handling if same
        if f1 > f2: return dist(f2, f1)
        return f2 - f1 - 1
    
    numJumps = 0
    for nextFrog in p[1:]:
        numJumps += dist(headFrog, nextFrog)
        headFrog = nextFrog
    
    # so now all 1 group
    numJumps += dist(headFrog, n) # get to n-1th lilipad, could be 0

    # Now all jump to end
    numJumps += f # number of frogs

    return numJumps

print(solve(6, 3, [5, 2, 4]))




    

