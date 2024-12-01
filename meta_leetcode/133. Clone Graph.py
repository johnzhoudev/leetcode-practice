"""

133. Clone Graph

connected undirected graph

deep copy

do a dfs - create neighbors if not created, store in hash table if created

O(n) time
O(n) space

Tactic:
use nodecopies hash table. DFS return node copy. the for neighbors append dfs(neighbor).

"""



class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solve(root):
    nodeCopies = {}
    if not root: return None

    def dfs(node):
        if node in nodeCopies: return nodeCopies[node]

        copy = Node(node.val)
        nodeCopies[node] = copy

        for neigh in node.neighbors:
            copy.neighbors.append(dfs(neigh))
        return copy
    
    return dfs(root)
        




