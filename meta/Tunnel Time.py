"""

Tunnel Time


- no tunnel touches or covers 0
- no 2 tunnels intersect or touch each other

- circular loop
- tunnels along the thing
- 1 m / s
- how many seconds before total tunnel time reaches k?

1. calculate total tunnel time in 1 loop
2. divide k by loop tunnel time, that's loop time
3. figure out offset time - just add 1 at a time

O(n)

Actually O(n log n) due to the sorting!


"""

def solve(C, N, A, B, k):
    # first, calculate total tunnel time

    # takes C seconds to go 1 loop
    tunnelTime = 0
    for b, a in zip(B, A):
        tunnelTime += (b-a)
    
    # figure out num loops
    numLoops = k // tunnelTime
    if k % tunnelTime == 0: # if perfect loop, final tunnel afterwards could have time. so say
        numLoops -= 1
    
    totalTime = numLoops * C
    k -= numLoops * tunnelTime

    # now figure out offset time
    tunnels = [(a, b) for a, b in zip(A, B)]
    tunnels.sort(key=lambda x : x[0]) # should be sorted by first

    lastTunnelEnd = 0
    for start, end in tunnels:
        if (k == 0): break

        # distance to get to tunnel
        totalTime += start - lastTunnelEnd

        # distance in tunnel
        totalTime += min(end - start, k)
        k -= min(end - start, k)

        lastTunnelEnd = end
    
    return totalTime


C = 10
N = 2
A = [1, 6]
B = [3, 7]
K = 7

C = 50
N = 3
A = [39, 19, 28]
B = [49, 27, 35]
K = 15

print(solve(C, N, A, B, K))