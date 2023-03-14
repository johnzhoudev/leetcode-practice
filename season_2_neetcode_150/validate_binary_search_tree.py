# Results:
# Runtime: 42ms 86.8%
# Memory Usage: 16.5MB 71.44%

"""

https://leetcode.com/problems/validate-binary-search-tree/

Idea:
- recursively check if valid, and produce largest and smallest of a tree
- have to do a postorder traversal, pretty much
- recursion
O(n) time, O(n) space - at any point in time, could have n recursions going

Idea 2: use valid range

Tactic: Use valid range, can check if each node satifsfies iteratively

"""

def solve(root):

    state = [(root, float("-inf"), float("inf"))]
    while state:
        node, minVal, maxVal = state.pop()
        if node is None: continue
        if node.val <= minVal or node.val >= maxVal:
            return False
        state += [(node.left, minVal, node.val), (node.right, node.val, maxVal)]
    return True


def solve(root):

    def dfs(node): # returns isValid, lowest, highest
        if node is None: return True, float("inf"), float("-inf")

        leftValid, leftSmall, leftHigh = dfs(node.left)
        rightValid, rightSmall, rightHigh = dfs(node.right)
        if not leftValid or not rightValid or leftHigh >= node.val or rightSmall <= node.val:
            return False, 0, 0
        return True, min(leftSmall, node.val), max(rightHigh, node.val)
    
    return dfs(root)[0]


