"""

339. Nested List Weight Sum

return sum of each int in nested list multipled by its depth

Just do a bfs?  with depth param

Time: O(n)
Space: O(n), or O(max width of a thing)

If dfs, mem would be O(depth)

I think dfs would be harder to implement with a stack. But recursively it could easily be done.
Actually not that bad

Tactic:
dfs or bfs.

"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

def solve(nestedList):

    toParse = [nestedList]
    total = 0
    depth = 0

    while toParse:
        nextToParse = []
        depth += 1

        for list in toParse:
            for elt in list:
                if elt.isInteger():
                    total += elt.getInteger() * depth
                else: # must be nested list
                    nextToParse.append(elt.getList())
            
        toParse = nextToParse
    
    return total

