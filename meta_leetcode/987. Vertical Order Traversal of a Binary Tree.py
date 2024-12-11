"""

987. Vertical Order Traversal of a Binary Tree

Just do bfs and add to columns?

If same coords, add to dummy array in hash table and append after

Better: Just use a table instead of an array for cols to left / right

Tactic:
Make columns, and bfs traversal append to columns, keep max and min col

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

def solve(root):
    if not root: return []

    cols = defaultdict(list)

    queue = deque()
    queue.append((root, 0))

    row = -1
    left = 0
    right = 0

    while queue:
        row += 1
        num = len(queue)

        for _ in range(num):
            node, offset = queue.popleft()
            if not node: continue
            cols[offset].append((row, node.val))
            queue.append((node.left, offset - 1))
            queue.append((node.right, offset + 1))

            left = min(left, offset)
            right = max(right, offset)
        
    result = []
    for i in range(left, right + 1):
        result.append([x for _, x in sorted(cols[i])])
    return result

def solve(root):
    if not root: return []

    colsToLeft = [] # inverted
    colsToRight = [] # regular

    # Now do bfs
    queue = deque()
    queue.append((root, 0))

    while queue:
        num = len(queue)

        leftCols = defaultdict(list)
        rightCols = defaultdict(list)

        # get all new values
        for _ in range(num):
            node, offset = queue.popleft()

            if not node: continue

            if offset >= 0:
                rightCols[offset].append(node.val)
            else:
                leftOffset = (-offset) - 1
                leftCols[leftOffset].append(node.val)

            # Now add left and right
            queue.append((node.left, offset - 1))
            queue.append((node.right, offset + 1))
        
        for leftOffset in leftCols:
            if leftOffset >= len(colsToLeft):
                colsToLeft.append([])
            colsToLeft[leftOffset].extend(sorted(leftCols[leftOffset]))
        
        for offset in rightCols:
            if offset >= len(colsToRight):
                colsToRight.append([])
            colsToRight[offset].extend(sorted(rightCols[offset]))
            
    
    return colsToLeft[::-1] + colsToRight



                

    