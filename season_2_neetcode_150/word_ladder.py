"""

https://leetcode.com/problems/word-ladder/

- have dict of words
- step words one by one, each differs by single letter
- go from beginword to end word, beginword not in dictionary
- return min num transformations

Ideas:
- brute force, search alg to check every single possibility
- DP with memoization, state is at x, what is shortest way to get to y?
    - O(x, y), so O(n^2) states
- have to use seen array. can't do loops. DFS.

- maybe build graph in the beginning? check if a word differs in one position
    - O(max len * n) to check all chars
So O(max len * n) to check all chars and make a graph, then O(n^2) dp with memoization

- DP ground up? 
    - dp[x][y] = shortest path from x to y
    - start with same len, [x][x] = 0
    - then as len increases, pick middle and go 
    - O(n^2) * O(n) per each, since have to evaluate where in the path you depart

- Use djikstra's alg, get shortest path from one place to all places
- O(n) time? for graph?


"""

def solve(begin, end, words):
    # add word begin
    if begin not in words:
        words.append(begin)

    # 0 for match, 1 for only 1, -1 for more
    def diff(s1, s2):
        diffCount = 0
        for i, c in enumerate(s1):
            if c != s2[i]:
                diffCount += 1
        return diffCount if diffCount < 2 else -1

    # first, build graph
    # adj = [[False for _ in range(len(words))] for _ in range(len(words))]
    adj = {}
    for word in words:
        adj[word] = {}

    for s1 in enumerate(words):
        for s2 in enumerate(words):
            dif = diff(s1, s2)
            if dif == 0 or dif == 1:
                adj[s1][s2] = True
    
    # do dijkstra's alg
    # reachable is hash from word to num steps to it
    reachable = {
        begin: 0
    }
    min_distances = {}
    for word in words:
        

    while reachable:
        minSteps = len(words) + 10
        minWord = ""
        for word in reachable:
            if reachable[word] < minSteps:
                minWord = word
                minSteps = reachable[word]
        
        assert minWord != ""
        # now have min
        min_distances


        
        

    
    
    # setup state
    # min dist between x, y
    # state = [[-1 for _ in range(len(words))] for _ in range(len(words))]
    # for x in range(len(words)):
    #     state[x][x] = 0
    

    


