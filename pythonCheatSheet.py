# Cheat sheet for python syntax

# Stacks using lists
stack = ["item1", "item2", "item3"]
stack.append("item4")
print(stack.pop())

# Queue using deque
from collections import deque
deque1 = deque()
deque1.append("item")
deque1.appendleft("nah")
print(deque1)
deque1.pop()
deque1.popleft()

# queue using list
queue1 = ["1", "2"]
queue1.append("3")
print(queue1.pop(0))

# Array extend and append
arr = [1, 2, 3]
arr += [4] # append
arr += [5, 6, 7] # extend
arr.extend([4, 5, 6])
arr.append(4)
print(arr)

# Enums
class Direction:
	LEFT = 0
	RIGHT = 1

print(Direction.LEFT)
print(Direction.RIGHT)

# Tree shortcuts
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def print(self):
      print(self.val)
      if (self.left): self.left.print()
      if (self.right): self.right.print()

# hash tables
table = {}
table = dict()
table[34] = 2
table["asdf"]= 3
print(table.items())
print(table.keys())
print(table.values())
if (34 in table):
	print("34 is in table")
del table["asdf"]

# iterate with indices
l = [1, 2, 3, 4, 5, 6]
for idx, x in enumerate(l):
	print(idx)
	print(x)

# heaps - min heap
import heapq

heap = []
heapq.heappush(heap, (2, "2"))
heapq.heappush(heap, (3, "3"))
heapq.heappush(heap, (4, "3"))
heapq.heappush(heap, (3, "3"))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
# smallest element always heap[0]


arr = [1, 2, 3, 4, 5]
arr.index(3) # 2

## Sets

thisSet = set()
thisSet.add('a')
if 'a' in thisSet:
      print("hi")
thisSet.remove('a')

# lists
list1 = [1, 2, 3, 4, 5, 10]
list1.remove(10)
del list1[2:3]
print(list1)

## strings
listOfStrings = ["asdf", "asdf"]
''.join(listOfStrings)