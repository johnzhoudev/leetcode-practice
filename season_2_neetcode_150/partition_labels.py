"""

https://leetcode.com/problems/partition-labels/

- partition string into as many parts so that each letter appears in at most one part


Ideas:
- advance thru, keep splitting into parts if not seen yet, but if seen, do a set union?
- disjoint union pretty much
    - but may have to union multiple parts, between
    - hash parent to part index and vice versa
    - rank and union algorithm

- find, just get parent until parent is self 
    - also compression, make other tihngs same parent along the way
- union, whichever has higher rank, make parent.

- hard part, how to union multiple parts?
- non-triv.

Idea 2: can be done O(n) and O(1) space? 2 pass
- problem is how to join multiple sections?

- when you consider a letter. If not seen yet, add it as it's own section
- if seen, use a map to the earliest occurrence of that letter. then also cross ref the starting points array and pop the ends until starting point < letter

Idea 3:
- Basically, only create a section once all the letters in that section are completely contained in that section
    - so do one pass to find last index of letters
    - then on 2nd pass, extend section until all letters are covered

Tactic: only create section once all letters in section are completely contained in section. Find last index of letters, and on 2nd pass, do.
"""

def solve(s):
    lastLetter = dict()
    for idx, c in enumerate(s):
        lastLetter[c] = idx
    
    # now traverse
    output = []
    minRight = 0
    size = 0
    
    # assuming i hasn't been added yet
    # minRight is min that right has to be at
    for i in range(len(s)):
        size += 1
        minRight = max(lastLetter[s[i]], minRight)
        if i == minRight:
            output.append(size)
            size = 0
    
    return output
    


def solve(s):
    letterMap = dict()
    output = []

    for idx, c in enumerate(s):
        if c not in letterMap:
            letterMap[c] = idx
            output += [idx] # contains starts of new sections
        else:
            # c is in lettermap, so need to merge with leftmost
            while output[-1] > letterMap[c]:
                output.pop()

    # now formalize output array. it has 
    for i in range(len(output)):
        if i+1 == len(output):
            output[i] = len(s) - output[i]
        else:
            output[i] = output[i+1] - output[i]
    
    return output


# Not finished, too complex
def solve(s):
    parent = dict()
    rank = dict()
    # for each letter, put in a parent

    def insert(c):
        parent[c] = c
        rank[c] = 0
        return c

    # auto inserts if not found
    def find(c):
        if c not in parent or c not in rank:
            raise RuntimeError()
        stackTrace = []
        while parent[c] != c:
            stackTrace.append(c)
            c = parent[c]
        for item in stackTrace:
            parent[item] = c # set as parent
        return c
    
    def union(c, d):
        par1 = find(c)
        par2 = find(d)
        if rank[par1] > rank[par2]:
            # attach 2 to 1
            parent[par2] = par1
            rank[par1] += 1
        else:
            parent[par1] = par2
            rank[par2] += 1
    
    for c in s:
        # add new thing
        if c not in parent:
            insert(c)
        else:
            part = find(c)
    
