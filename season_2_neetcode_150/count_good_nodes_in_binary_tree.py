# Results:
# Runtime: 256ms 68.82%
# Memory Usage: 32.6MB 35.84%

"""

https://leetcode.com/problems/count-good-nodes-in-binary-tree/


good = no nodes in path with value greater than node

Idea: do dfs, keep track of max value seen in path
O(n) time, O(n) space if we store max val

Tactic: DFS, track maxValue

"""

def solveRecursive(root):

    def dfs(node, maxVal): # returns number of good nodes
        if node is None: return 0
        maxVal = max(maxVal, node.val)
        return dfs(node.left, maxVal) + dfs(node.right, maxVal) + (1 if node.val >= maxVal else 0)
    
    return dfs(root, root.val) if root else 0


# too slow! - is iteration slower than recursion?
def solve(root):
    if root is None: return 0
    state = [(root, root.val)]
    count = 0
    while state:
        node, maxVal = state.pop() # maxVal doesn't include node yet
        if node is None: continue
        if node.val >= maxVal:
            count += 1
        maxVal = max(maxVal, node.val)
        state += [(node.left, maxVal), (node.right, maxVal)]
    return count
