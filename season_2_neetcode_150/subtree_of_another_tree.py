# Results:
# Runtime: 125ms 61.63%
# Memory Usage: 15.1MB 29.23%

"""

https://leetcode.com/problems/subtree-of-another-tree/

idea:
- Brute force, check for each node, O(n * m)
- Might have to. no way we can remove possibilities by only looking once?
- Yolo. brute force might be best tbh

Tactic: So you could make a hash and string compare. But straightforward way is check same for each node.

"""

def solveRecursive(root, subRoot):
    
    def checkEqual(p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False
        return checkEqual(p.left, q.left) and checkEqual(p.right, q.right)
    
    if checkEqual(root, subRoot): return True
    if root:
        return solveRecursive(root.left, subRoot) or solveRecursive(root.right, subRoot)
    return False
        



def solve(root, subRoot):
    starts = [root]

    def checkEqual(p, q):
        state = [(p, q)]
        while state:
            n1, n2 = state.pop()
            if n1 is None or n2 is None:
                if n1 != n2:
                    return False
            elif n1.val != n2.val:
                return False
            else:
                state += [(n1.left, n2.left), (n1.right, n2.right)]
        return True

    while starts:
        start = starts.pop()
        if checkEqual(start, subRoot):
            return True
        if start: starts += [start.left, start.right]
    return False
