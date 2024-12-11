"""

127. Word Ladder

differ by single letter
shortest transform
or 0 if none exists


Graph problem, word to other word adj list
- for word, * method to store hash table to words like that

Do a bfs, with visited

Time:
O(n m) to make adj list thing
O(n m) for bfs

Tactic:
Use wildcard * to map to adj words. Then BFS with visited. Find endidx too?

"""

from collections import defaultdict, deque

def solve(begin, end, wordlist):
    # check
    if begin == end: return 0

    adjlist = defaultdict(list) # store word* => list of idx's of words it connects to
    endIdx = -1
    # Make adj list thing
    for idx, word in enumerate(wordlist):
        for i in range(len(word)):
            newword = word[:i] + "*" + word[i+1:] # can be done in c++ in O(m*n)
            adjlist[newword].append(idx)

        # set
        if endIdx == -1 and end == word:
            endIdx = idx
    
    # Now do bfs
    visited = set()
    queue = deque()
    queue.append(begin)
    visited.add(begin)

    steps = 0
    while queue:
        n = len(queue)
        steps += 1

        # for each word in state
        for i in range(n):
            # new word, so add
            word = queue.popleft() # already in visited

            # for each possible combo, add next words
            for i in range(len(word)):
                newword = word[:i] + "*" + word[i+1:]

                if newword in adjlist:
                    for next in adjlist[newword]:

                        if next == endIdx: # terminate if found
                            return steps + 1

                        if wordlist[next] not in visited:
                            queue.append(wordlist[next])
                            visited.add(wordlist[next]) # avoid adding duplicates
    
    return 0
            
                    






