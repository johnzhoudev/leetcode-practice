"""

133. Clone Graph

connected undirected graph

Make a deep copy

Idea:
- keep hash table of created nodes
- dfs, create a new node for each node visited?
  - create a new node
  - dfs at that node
  - then add the connection

O(n) time

Tactic: DFS, use hash table to store copied nodes. Make sure to put nodeCopy in map to prevent infinite recursion.

"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] # list of nodes

def solveIterative(node: Node):
    nodeCopyMap = {}
    if node is None: return None
    stack = [node]
    nodeCopyMap[node.val] = Node(node.val) # create first copy

    while stack: # when process a node, create node and create all neighbors and add neighbors to stack
        curr = stack.pop()

        copy = nodeCopyMap[curr.val] # node should already exist, just not processed yet

        neighbors = []

        for neigh in curr.neighbors:
            if neigh.val not in nodeCopyMap:
                neighCopy = Node(neigh.val)
                nodeCopyMap[neigh.val] = neighCopy
                stack.append(neigh) # process neighbor next

            neighbors.append(nodeCopyMap[neigh.val])

        copy.neighbors = neighbors
    
    return nodeCopyMap[node.val]


def solve(node):
    nodeCopyMap = {} # val to node
  
    def dfs(node):
        if not node: return None
        if node.val in nodeCopyMap:
            return nodeCopyMap[node.val]
        
        # Else create
        copyNode = Node(node.val)
        nodeCopyMap[node.val] = copyNode

        neighbors = []

        for neigh in node.neighbors:
            if neigh.val in nodeCopyMap:
                neighbors.append(nodeCopyMap[neigh.val])
            else:
                newNode = dfs(neigh) 
                nodeCopyMap[neigh.val] = newNode
                neighbors.append(newNode)

        copyNode.neighbors = neighbors
        
        return copyNode

    return dfs(node)



    

      
    


