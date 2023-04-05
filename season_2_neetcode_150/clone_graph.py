"""

https://leetcode.com/problems/clone-graph/

- deep copy connected undirected graph
- each node has value and list of neighbours
    - node value is unique

Idea:
- dfs, at each node
    - first process other nodes to create them
    - then once created, add neighbours
- maintain hash table of nums to neighbour references

Time: O(n), space: O(n) to store references
- can you do in O(1)? - could return the node from DFS and add. But how to tell if a node is created? Can't. Need to keep set.

Can also do iterative if you create all the neighbours when you hit node

Tactic: Use map to map nums to nodes. DFS, either recursive or iterative.

"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solveIter(originalNode):

    if originalNode is None:
        return None
    
    nodes = {}
    nodes[originalNode.val] = Node(originalNode.val)
    state = [originalNode]

    # creates child nodes and also adds neighbours
    while state:
        node = state.pop()
        # add neighbours
        nodeCopy = nodes[node.val]
        for neigh in node.neighbors:
            if neigh.val not in nodes:
                nodes[neigh.val] = Node(neigh.val)
                # append child node to state to process
                state.append(neigh)
            nodeCopy.neighbors.append(nodes[neigh.val])
    
    return nodes[originalNode.val]
       

def solve(originalNode):
    if originalNode is None:
        return None

    # state
    nodes = {} # map node value to new reference

    def dfs(node):
        nonlocal nodes
        if node.val in nodes:
            return nodes[node.val]
        
        newNode = Node(node.val)
        nodes[node.val] = newNode

        for neigh in node.neighbors:
            newNode.neighbors.append(dfs(neigh)) # gets existing or makes new

        return newNode

    return dfs(originalNode)