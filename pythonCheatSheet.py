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
arr += [4]
arr.extend([4, 5, 6])
arr.append(4)
print(arr)

# Enums
class Direction:
	LEFT = 0
	RIGHT = 1

print(Direction.LEFT)
print(Direction.RIGHT)