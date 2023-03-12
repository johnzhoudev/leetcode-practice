# Results:
# Runtime: 116ms 77.21%
# Memory Usage: 20.3MB 60.99%

"""

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Idea 1: level by level, row by row, and fill in nulls where necessary
- do bfs pretty much from root, and read off
- O(n), O(n)

Idea2:
- traversal, and back

Tactic: Do a bfs, record nodes as they come and rebuild by popping from a queue and adding nodes. Careful with stripping and delimiters!

"""
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        output = ""
        q = deque()
        q.append(root)
        while q:
            count = len(q)
            for _ in range(count):
                node = q.popleft()
                if node:
                    output += str(node.val) + ","
                    q.append(node.left)
                    q.append(node.right)
                else:
                    output += ","
        return output # will contain extra ","
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == ",":
            return None # no root edge case
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        i = 1
        while i < len(data) - 1:
            parent = q.popleft()
            parent.left = TreeNode(int(data[i])) if data[i] != "" else None
            parent.right = TreeNode(int(data[i + 1])) if data[i + 1] != "" else None

            if parent.left:
                q.append(parent.left)
            if parent.right:
                q.append(parent.right)

            i += 2 # take pairs
        
        return root

