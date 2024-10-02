"""

words are sorted in new language 
abc...z
- a smaller than b if 
    - first letter differ smaller in a than in b
    - or same word and a.length < b.length

Can basically form a directed acyclic graph
- given 2 words, either same prefixes or first character difference, you can tell alphabetically
- cycle => incorrect order
- otherwise just looking for directed acyclic graph

- Becomes finding an ordering. topological sort

Tactic:
First character differ => c1 < c2. Then build directed graph and do topological sort with indegrees. Or use recursive dfs, and push onto output once all neighbours visited, then reverse.

"""

from collections import defaultdict
def solve(words):
    # first, compare all pairs of words and add ordering to graph
    adjList = defaultdict(set)
    indegrees = defaultdict(lambda : 0)
    characters = set()

    # Add all characters
    for word in words:
        for c in word:
            characters.add(c)

    # Provided w1 < w2 => either differing character, or w1 < w2 length
    def getDifferingCharacters(w1, w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return (w1[i], w2[i])
        
        return None, None


    for idx, word in enumerate(words[:-1]):
        word2 = words[idx + 1]
        try:
            c1, c2 = getDifferingCharacters(word, word2)
        except Exception as e:
            return "" # failed to get diff, not possible ordering
        if c1 is not None and c2 not in adjList[c1]:
            adjList[c1].add(c2)
            indegrees[c2] += 1
        
    # Now do topological sort, and add any other characters afterwards
    # Topological sort by dfs, using indegrees
    state = []
    for c in characters:
        if indegrees[c] == 0:
            state.append(c)
    
    # If contains a cycle, indegree will never be zero so will not get all chars
    output = []
    while state:
        c = state.pop()
        output.append(c)

        for nextc in adjList[c]:
            indegrees[nextc] -= 1
            if indegrees[nextc] == 0:
                state.append(nextc)
    
    return ''.join(output) if len(output) == len(characters) else ""


from collections import defaultdict
def solve(words):
    # first, compare all pairs of words and add ordering to graph
    adjList = defaultdict(set)
    indegrees = defaultdict(lambda : 0)
    characters = set()

    # Add all characters
    for word in words:
        for c in word:
            characters.add(c)

    # Provided w1 < w2 => either differing character, or w1 < w2 length
    def getDifferingCharacters(w1, w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return (w1[i], w2[i])
        
        return None, None


    for idx, word in enumerate(words):
        for word2 in words[idx + 1:]:
            # word <= word2
            try:
                c1, c2 = getDifferingCharacters(word, word2)
            except Exception as e:
                return "" # failed to get diff, not possible ordering
            if c1 is not None and c2 not in adjList[c1]:
                adjList[c1].add(c2)
                indegrees[c2] += 1
        
    # Now do topological sort, and add any other characters afterwards
    # Topological sort by dfs, using indegrees
    state = []
    for c in characters:
        if indegrees[c] == 0:
            state.append(c)
    
    # If contains a cycle, indegree will never be zero so will not get all chars
    output = []
    while state:
        c = state.pop()
        output.append(c)

        for nextc in adjList[c]:
            indegrees[nextc] -= 1
            if indegrees[nextc] == 0:
                state.append(nextc)
    
    return ''.join(output) if len(output) == len(characters) else ""



    
    
