"""

133. Clone Graph


connected undirected graph
deep copy of graph?

do dfs, keep map of reference to new node.
then update references

O(n)

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solve(root):
    if not root:
        return None

    node_map = {}
    node_map[root] = Node(val=root.val)

    # Just do dfs, and create node copies with empty neighbors

    state = [root]

    while state:
        node = state.pop()
        # Node already in node map
        for neighbor in node.neighbors:
            if neighbor in node_map:
                continue
            node_map[neighbor] = Node(val=neighbor.val)
            state.append(neighbor)
    
    # Now fill in
    for node in node_map:
        node_map[node].neighbors = [node_map[neigh] for neigh in node.neighbors]
    
    return node_map[root]




