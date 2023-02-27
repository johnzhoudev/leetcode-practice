# Results:
# Runtime: 60ms 79.24%
# Memory Usage: 18.1MB 52.50%

"""

https://leetcode.com/problems/min-stack/

push pop top getMin, all in O(1)

Idea:
- stack can only push and pop from top
- could have 2 stacks, one for the value, and one for the min at the current level
    - when push, just check last min and current value
- Difficulty is when you pop the min, then how do you calculate new min? and deal with duplicates

Tactic: Use 2 stacks, one for val and one for minval. Or store as tuples

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if (len(self.minstack) == 0):
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]