
"""

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


Preorder and inorder? - O(n) storage
String of calls, with brackets? - also O(n), each value will have at most () and ()
- stored node(left)(right)

Naive: Just store root, left and right


First Attempt:
- Do a recursive DFS, and serialize a node as (val, (<left>)(<right>))
- O(n) space since each node will generate 3 sets of ()
- O(n) to deserialize
- Parsing is just a bit skibidi

Tactic: DFS, and csv with empty nodes as N. Then deserialize with another DFS, greedy taking nodes. Will naturally use up elements.

"""


# Better - just do dfs, and store as an array. Deserializing will naturally use up elements as you go.

# Definition for a binary tree node.
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
        output = []
        def dfs(node):
            nonlocal output
            if not node:
                output.append("N")
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            if nodes[idx] == 'N':
                idx += 1
                return None
            val = int(nodes[idx])
            ret = TreeNode(val)
            idx += 1
            ret.left = dfs()
            ret.right = dfs()
            return ret
        
        return dfs()



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class CodecOld:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "()"
        
        s = str(root.val)
        s += f"{self.serialize(root.left)}"
        s += f"{self.serialize(root.right)}"
        return f"({s})"

    def get_value_and_inner(self, s): # s in form (val()())
        val = ""
        idx = 0
        assert s[idx] == '('
        idx += 1
        while s[idx] != '(':
            val += s[idx]
            idx += 1
        val = int(val)
        # Idx is now on (
        left = "("
        idx += 1 # Skip (
        openCount = 1
        while openCount != 0:
            if s[idx] == '(':
                openCount += 1
            elif s[idx] == ')':
                openCount -= 1
            left += s[idx]
            idx += 1
        # Now idx one past last ), should be on next (
        assert s[idx] == '('

        right = "("
        openCount = 1
        idx += 1

        while openCount != 0:
            if s[idx] == '(':
                openCount += 1
            elif s[idx] == ')':
                openCount -= 1
            right += s[idx]
            idx += 1
        
        return val, left, right, idx + 1 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "()":
            return None
        assert data[0] == '('
        val, left, right, nextIdx = self.get_value_and_inner(data)
        ret = TreeNode(val)
        ret.left = self.deserialize(left)
        ret.right = self.deserialize(right)
        return ret

        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
x = TreeNode(4)
x.left = TreeNode(3)

ans = ser.serialize(x)
print(ans)
r = ser.deserialize(ans)
print(ser.serialize(r))
