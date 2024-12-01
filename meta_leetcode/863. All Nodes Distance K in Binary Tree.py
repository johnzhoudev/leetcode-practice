"""

863. All Nodes Distance K in Binary Tree

distance k from target node

- first step is to find target node


- Find target node
    - if found, search left and right x distance
    - when returning, if found, do search for distance less

O(n) time complexity
O(h) space complexity (dfs)

Can also do with a hash map and build a graph. Then bfs from graph.

Tactic:
Fancy: dfs, param maxDist=None if not found yet. Once found, do dfs with maxDist and update. Else, make hash table adj list from nodes and do dfs / bfs in 2nd pass

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
def solve(root, target, k):

    # first build graph
    adjLists = defaultdict(list)

    def buildGraph(node):
        nonlocal adjLists
        if not node: return
        # add back links
        if node.left:
            adjLists[node].append(node.left)
            adjLists[node.left].append(node)
            buildGraph(node.left)
        if node.right:
            adjLists[node].append(node.right)
            adjLists[node.right].append(node)
            buildGraph(node.right)
    buildGraph(root)

    # Now do dfs from target node
    output = []
    visited = set()
    def dfs(node, k):
        nonlocal output
        nonlocal visited
        nonlocal adjLists

        if node in visited: return
        visited.add(node)

        if k < 0:
            return
        elif k == 0:
            output.append(node.val)
            return # can't continue exploring
        else:
            for nextNode in adjLists[node]:
                dfs(nextNode, k - 1)
    dfs(target, k)
        
    return output


        
def solve(root, target, k):

    output = []

    # returns distance you can search from there, or None if not found
    # maxDist will be number of steps you can take from here.
    def dfs(node, maxDist = None):
        nonlocal output

        if not node: return None

        # maxDist being valid indicates target is found
        if maxDist and maxDist == -1: return None  # already taken too many steps.

        # target found, 
        if node == target:

            if k == 0:
                output.append(node.val)

            # need to search recursively in branches with maxDist
            if node.left: dfs(node.left, k - 1) # can take at most k-1 steps from the node
            if node.right: dfs(node.right, k - 1)
            return k-1 # can take k-1 steps from parent
        
        # Now do regular search
        if maxDist is not None: # target already found
            if maxDist == 0:
                output.append(node.val)
                return None

            # otherwise continue exploring
            if node.left: dfs(node.left, maxDist - 1) # can take at most k-1 steps from the node
            if node.right: dfs(node.right, maxDist - 1)
        else:
            left = dfs(node.left) if node.left else None

            if left is not None: # found on left
                if left == 0:
                    output.append(node.val)
                    return None # done search
                else:
                    if node.right: dfs(node.right, left - 1)
                    return left - 1

            right = dfs(node.right) if node.right else None
            if right is not None: # found on left
                if right == 0:
                    output.append(node.val)
                    return None # done search
                else:
                    if node.left: dfs(node.left, right - 1)
                    return right - 1
    
    dfs(root)
    return output



